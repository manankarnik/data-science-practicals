df <- read.csv("movies.csv")
df <- na.omit(df)
# Reduce data to 10 records for better plot
df <- df[1:10, ]
# Convert VOTES column from string to int
df$VOTES <- as.integer(gsub(",", "", df$VOTES))

pie(df$VOTES, labels = df$MOVIES, main = "Votes")
