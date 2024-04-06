data <- read.csv("jobs.csv")
data$Month <- as.Date(paste0(data$Month, "01"), format="%YM%m%d")
x <- data$Month
Y <- data$Total.Filled.Jobs
d.y <- diff(Y)
plot(x, Y)

acf(Y)
pacf(Y)
acf(d.y)

arima(Y, order = c(1, 0, 1))
arima(Y, order = c(0, 0, 1))
data.arima001 <- arima(Y, order = c(0, 0, 1))
data.pred1 <- predict(data.arima001, n.ahead = 100)
plot(Y)

# The blue line is the future prediction.
lines(data.pred1$pred, col = "blue")

head(data.pred1)
tail(data.pred1)

head(data.pred1$pred)
tail(data.pred1$pred)
