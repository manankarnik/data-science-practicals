df <- read.csv("movies.csv")
df <- na.omit(df)
# Convert Gross column from string to float
df$Gross <- as.numeric(gsub("[$M]", "", df$Gross))

boxplot(df$Gross, df$RunTime,
        main = "Boxplot of Gross and RunTime",
        names = c("Gross", "RunTime"),
        ylab = "Values")
