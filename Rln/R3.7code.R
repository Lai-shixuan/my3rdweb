# 所需要用到的包
library(reshape2)
library(agricolae)
library(ggplot2)

# AOV
data <- matrix(c(3129, 3000, 2865, 2890,
                3200, 3300, 2975, 3150,
                2800, 2900, 2985, 3050,
                2600, 2700, 2600, 2765), nrow = 4, byrow=TRUE)
rownames(data) <- c("TE1", "TE2", "TE3", "TE4")  # 表行命名
str(data)
datalg <- melt(data)
colnames(datalg) <- c("trt", "rep", "number")
datalg_aov <- aov(number ~ trt, datalg)
summary(datalg_aov)

# 均值并作图
ag <- aggregate(number ~ trt, datalg, mean)
windows()
sd <- summary(datalg_aov)[[1]]$'Mean Sq'[2]
mul <- sqrt(sd/5)
x <- seq(-10, 10, 0.5)
y <- dt(x, df = df.residual(datalg_aov)) # mean = 3000, sd = summary(datalg_aov)[[1]]$'Mean Sq'[2])
plot(x*mul + 3000  , y, xlim = c(2600, 3400))
points(x = ag$number, y = c(0, 0, 0, 0))


# LSD
shape <- dim(data)
a <- shape[1]
n <- shape[2]
N <- a * n
SST <- sum(datalg$number^2) - sum(datalg$number)^2 / N
SSTrt <- (sum(aggregate(number ~ trt, datalg, sum)$number^2) / n - sum(datalg$number)^2 / N)
SSE <- SST - SSTrt
MSTrt <- SSTrt / (a-1)
MSE <- SSE / (N-a)

LSD <- qt(1-0.05/2, N-a) * sqrt(2 * MSE / n)
LSD
LSD.test(datalg_aov, "trt", group = FALSE, console = TRUE)

# 正态假设
setwd("D:\\GoogleDrive\\05 r\\Code(first 6 chapters)for Douglas-C.-Montgomery-Design-and-Analysis-of-Expe_2")
source("Chapter3/PP_plot.R")
windows()
datalg_res = residuals(datalg_aov)
pp.plot(datalg_res, pch = 10, lty = 1, xlab = "Residual", line.method = "Q", legend.add = FALSE)

shapiro.test(datalg_res)

# 残差随预测压强的分布图
plot(datalg_res ~ datalg_aov$fitted.values, pch = 22, xlab = "Tensile Strength", ylab = "Residuals")
abline(h = 0)

# 残差随实值的变化
plot(datalg_res ~ datalg$number, pch = 22, xlab = "Tensile Strength", ylab = "Residuals")
abline(h = 0)

#  方差齐性

bartlett.test(datalg$number ~ datalg$trt, data = datalg)

# 展示数据
df <- data.frame(trt = datalg$trt, tensile = datalg$number)
ggplot(data = df, mapping = aes(x = trt, y = tensile)) + geom_point()