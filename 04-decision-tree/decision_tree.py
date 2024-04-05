import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, auc, accuracy_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import graphviz

# Read dataset
titanic = pd.read_csv("titanic.csv").dropna(subset=["Survived"])
print(titanic.describe())
print(titanic.columns)

# Factorize columns
label_encoder = LabelEncoder()
titanic["Sex"] = label_encoder.fit_transform(titanic["Sex"])
titanic["Survived"] = label_encoder.fit_transform(titanic["Survived"])
titanic["Embarked"] = label_encoder.fit_transform(titanic["Embarked"])

# Divide into train and test set
x_train, x_test, y_train, y_test = train_test_split(titanic[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]], titanic["Survived"], test_size=0.2, random_state=0)

# Train decision tree classifier
clf = DecisionTreeClassifier(random_state=42).fit(x_train, y_train)

# Plot tree
dot_data = export_graphviz(clf, out_file=None, feature_names=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"], filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("tree")

# Pruning
cf_pruned = DecisionTreeClassifier(random_state=42, max_depth=5, min_samples_split=10, min_samples_leaf=5).fit(x_train, y_train)
dot_data = export_graphviz(cf_pruned, out_file=None, feature_names=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"], filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("tree_pruned")

# Evaluate model
y_pred = clf.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred) * 100
print(f"Confusion Matrix: {cm}")
print(f"Accuracy: {accuracy}")

# ROC curve
y_probs = clf.predict_proba(x_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, color="darkorange", lw=2, label="ROC curve (area = {:.2f})".format(roc_auc))
plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver Operating Characteristic (ROC) Curve")
plt.legend(loc="lower right")
plt.show()

