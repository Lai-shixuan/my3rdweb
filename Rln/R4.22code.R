library(reshape2)
data4_22 <- data.frame(value = c(8, 7, 1, 7, 3,
                                 11, 2, 7, 3, 8,
                                 4, 9, 10, 1, 5,
                                 6, 8, 6, 6, 10,
                                 4, 2, 3, 8, 8),
                       trt = c("A", "B", "D", "C", "E",
                               "C", "E", "A", "D", "B",
                               "B", "A", "C", "E", "D",
                               "D", "C", "E", "B", "A",
                               "E", "D", "B", "A", "C"),
                       day = rep(c(1:5), 5),  # rep是repeat函数的意思
                       batch = c(rep(1, 5), rep(2, 5), rep(3, 5), rep(4, 5), rep(5, 5)))
head(data4_22)  # 展示前5行，以检查导入数据正确
tail(data4_22)  # 展示后5行
data4_22_aov <- aov(value ~ factor(trt) + factor(batch) + factor(day), data4_22)  # 设置3个变量，1个数值
summary(data4_22_aov)

# 正态假设
setwd("D:\\GoogleDrive\\05 r\\Code(first 6 chapters)for Douglas-C.-Montgomery-Design-and-Analysis-of-Expe_2")
source("Chapter3/PP_plot.R")
windows()
data4_22_res <- residuals(data4_22_aov)
pp.plot(data4_22_res, pch = 10, lty = 1, xlab = "Residual", line.method = "Q", legend.add = FALSE)

shapiro.test(data4_22_res)

# 残差随预测压强的分布图
plot(data4_22_res ~ data4_22_aov$fitted.values, pch = 22, xlab = "Tensile Strength", ylab = "Residuals")
abline(h = 0)

# 残差随实值的变化
plot(data4_22_res ~ data4_22$value, pch = 22, xlab = "Tensile Strength", ylab = "Residuals")
abline(h = 0)

#  方差齐性

bartlett.test(data4_22$value ~ data4_22$trt, data = data4_22)