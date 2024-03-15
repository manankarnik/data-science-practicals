df <- read.csv("movies.csv")
df <- na.omit(df)

min_max_scaling <- function(column, new_min, new_max) {
  return ((column - min(column)) / (max(column) - min(column)) * (new_max - new_min) + new_min)
}

df$SCALED_RATING <- min_max_scaling(df$RATING, 1, 10)
print(head(df))
