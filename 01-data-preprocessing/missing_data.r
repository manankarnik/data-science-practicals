df <- read.csv("movies.csv")
print(head(df))

if (any(is.na(df$RunTime))) {
  cat("Column with missing values\n")
  print(head(df$RunTime))
  df$RunTime[is.na(df$RunTime)] <- mean(df$RunTime, na.rm = TRUE)
  cat("Missing values filled with the mean\n")
  print(head(df$RunTime))
} else {
  cat("No missing values in the column\n")
}