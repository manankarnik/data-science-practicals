df <- read.csv("movies.csv")
cat("Records:", nrow(df), "\n")
df <- unique(df)
cat("Records after dropping duplicates:", nrow(df), "\n")