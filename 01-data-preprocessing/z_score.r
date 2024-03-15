df <- read.csv("movies.csv")
df <- na.omit(df)
df$SCALED_RATING <- scale(df$RATING)
head(df)
