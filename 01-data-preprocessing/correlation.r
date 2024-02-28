library(ggplot2)

df <- read.csv("movies.csv")
print(df)
df[df==""] <- NA
df <- na.omit(df)
df$VOTES <- as.integer(gsub(",", "", df$VOTES))

print(nrow(df))
correlation <- cor(df$RATING, df$VOTES, method = c("pearson"))
cat("Correlation coefficient:", round(correlation, 2), "\n")

ggplot(df, aes(x = RATING, y = VOTES)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Scatter plot of Rating vs Votes",
       x = "Rating",
       y = "Votes") +
  annotate("text", x = min(df$RATING), y = max(df$VOTES), label = paste("Pearson Correlation:", round(correlation, 2)), hjust = 0, vjust = 1)
