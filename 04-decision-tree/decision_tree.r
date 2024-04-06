# Install packages
install.packages("partykit")
install.packages("caret")
install.packages("pROC")
install.packages('rattle')
install.packages('rpart.plot')
install.packages('RColorBrewer')

# Read dataset
titanic <- read.csv("titanic.csv")
summary(titanic)
names(titanic)

# Factorize columns
titanic$Sex <- as.factor(titanic$Sex)
titanic$Survived <- as.factor(titanic$Survived)
titanic$Embarked <- as.factor(titanic$Embarked)

# Sample dataset
pd <- sample(2, nrow(titanic), replace = TRUE, prob = c(0.8, 0.2))
pd

# Divide into train and test set
train_set <- titanic[pd == 1,]
test_set <- titanic[pd == 2,]

# Remove nulls
train_set <- train_set[complete.cases(train_set$Survived),]
test_set <- test_set[complete.cases(test_set$Survived),]

# Plot tree
library("partykit")
tree <- ctree(formula = Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, data= train_set)
plot(tree)

# Pruning
tree <- ctree(formula = Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, data = train_set,control = ctree_control(mincriterion = 0.99, minsplit = 500))
plot(tree)
pred <- predict(tree, test_set, type = "prob")
pred

# Ensure that both vectors have the same length
pred <- predict(tree, test_set)
pred <- pred[complete.cases(test_set$Survived)]
survived <- test_set$Survived[complete.cases(test_set$Survived)]

library("caret")
confusionMatrix(pred, survived)

# Predict on the entire test set including missing values
pred_prob <- predict(tree, test_set, type = "prob")

# Extract the predicted probabilities for the positive class
pred_probabilities <- as.numeric(pred_prob[, "1"])

# Compute the ROC curve
library("pROC")
roc_curve <- roc(test_set$Survived, pred_probabilities)

# Plot the ROC curve
plot(roc_curve)

library(rpart)
fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, data = titanic, method = "class")
plot(fit)
text(fit)

library(rattle)
library(rpart.plot)
library(RColorBrewer)
fancyRpartPlot(fit)
prediction <- predict(fit, titanic, type = "class")
prediction