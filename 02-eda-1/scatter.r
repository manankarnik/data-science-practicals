df <- read.csv("movies.csv")
df <- na.omit(df)
# Convert VOTES column from string to int
df$VOTES <- as.integer(gsub(",", "", df$VOTES))
# Convert Gross column from string to float
df$Gross <- as.numeric(gsub("[$M]", "", df$Gross))

# Plot scatter plot
plot(df$VOTES, df$Gross,
     xlab = "Votes",
     ylab = "Gross (Millions)",
     main = "Scatter Plot of Votes vs Gross")

abline(lm(df$VOTES ~ df$Gross), data = df)
