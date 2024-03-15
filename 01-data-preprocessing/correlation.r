df <- read.csv("movies.csv")
df <- df[complete.cases(df$RATING, df$VOTES), ]
df$VOTES <- as.integer(gsub(",", "", df$VOTES))

correlation <- cor(df$RATING, df$VOTES, method = c("pearson"))
cat("Correlation coefficient:", round(correlation, 2), "\n")

plot(df$RATING, df$VOTES, main = "Scatter plot of Rating vs Votes", xlab = "Rating", ylab = "Votes")

fit <- lm(VOTES ~ RATING, data = df)
abline(fit, col = "blue")

text(min(df$RATING), max(df$VOTES), labels = paste("Pearson Correlation:", round(correlation, 2)), pos = 4)
