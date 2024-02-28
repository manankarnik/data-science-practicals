df <- read.csv("movies.csv")
df$VOTES <- as.integer(gsub(",", "", df$VOTES))
df$Gross <- as.numeric(gsub("[$M]", "", df$Gross))
df <- df[complete.cases(df$VOTES, df$Gross), ]

numeric_df <- df[sapply(df, is.numeric)]
corr_matrix <- cor(numeric_df)

library(heatmaply)
heatmaply(corr_matrix, main = "Correlation Matrix")
