df <- read.csv("movies.csv")
df <- na.omit(df)
# Convert VOTES column from string to integer
df$VOTES <- as.integer(gsub(",", "", df$VOTES))

hist(df$VOTES, breaks = 10, xlab = "Votes", ylab = "Frequency", main = "Histogram of Votes")

# Reduce data to 10 records for better plot
df <- df[1:10, ]
barplot(df$VOTES, names.arg = df$MOVIES, xlab = "Movies", ylab = "Votes", main = "Bar Plot of Votes")

