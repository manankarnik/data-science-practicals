df <- read.csv("movies.csv")
chi_sq_result <- chisq.test(df$RATING, df$VOTES)

print(chi_sq_result)

alpha <- 0.5

if (chi_sq_result$p.value < alpha) {
  print("Null Hypothesis: Rejected (both values are dependent)")
} else {
  print("Null Hypothesis: Accepted (both values are independent)")
}
