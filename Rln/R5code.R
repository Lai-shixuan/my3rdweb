# lib
library(reshape2)
library(agricolae)
library(ggplot2)

data <- matrix(c(0.2, 74, 79, 82, 99,
                0.2, 64, 68, 88, 104,
                0.2, 60, 73, 92, 96,
                0.25, 92, 98, 99, 104,
                0.25, 86, 104, 108, 110,
                0.25, 88, 88, 95, 99,
                0.30, 99, 104, 108, 114,
                0.30, 98, 99, 110, 111,
                0.30, 102, 95, 99, 107), nrow = 9, byrow = TRUE)
data <- as.data.frame(data)
colnames(data) <- c("rate", "0.15", "0.18", "0.20", "0.25")  # 表行命名
data <- melt(data, id.vars = c("rate") ,variable.name="depth",value.name="value")
str(data)

data_aov <- aov(data$value ~ factor(data$depth) * factor(data$rate), data)
summary(data_aov)

# 模型检验

windows()

setwd("D:\\GoogleDrive\\05 r\\Code(first 6 chapters)for Douglas-C.-Montgomery-Design-and-Analysis-of-Expe_2")
source("Chapter3/PP_plot.R")
data_res <- residuals(data_aov)
pp.plot(data_res, pch = 10, lty = 1, xlab = "Residual", line.method = "Q", legend.add = FALSE)

shapiro.test(data_res)

plot(data_aov$fitted.values, residuals(data_aov), pch = 22, xlab = "fitted values", ylab = "Residuals")
abline(h = 0)


plot(data$rate, residuals(data_aov), pch = 22, xlab = "rate", ylab = "Residuals")
abline(h = 0)

plot(as.numeric(as.character(data$depth)), residuals(data_aov), pch = 22, xlab = "depth", ylab = "Residuals")
abline(h = 0)

# bartlett.test(data$value ~ as.numeric(as.character(data$rate)) * as.numeric(as.character(data$depth)))
# bartlett.test(data$value ~ as.numeric(as.character(data$depth)))

# 点估计

aggregate(data$value ~ data$rate, data, mean)

# 多重比较

data_0.2 <- subset(data, rate == 0.2)
data_0.2.Tukey <- with(data_0.2, HSD.test(y = value, trt = depth, DFerror = df.residual(data_aov),
                                          MSerror = (deviance(data_aov) / df.residual(data_aov)),
                                          group = FALSE))
data_0.2.Tukey$statistics
data_0.2.Tukey$comparison

data_0.25 <- subset(data, rate == 0.25)
data_0.25.Tukey <- with(data_0.2, HSD.test(y = value, trt = depth, DFerror = df.residual(data_aov),
                                          MSerror = (deviance(data_aov) / df.residual(data_aov)),
                                          group = FALSE))
data_0.25.Tukey$statistics
data_0.25.Tukey$comparison