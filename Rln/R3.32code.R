# libraries

library(reshape2)
library(agricolae)

# aov

data2 <- data.frame(p1 = c(2.76, 5.67, 4.49), p2 = c(1.43, 1.70, 2.19),
                   p3 = c(2.34, 1.97, 1.47), p4 = c(0.94, 1.36, 1.65))
str(data2)
data2lg <- melt(data2)
colnames(data2lg) <- c("pos", "value")
data2lg_aov <- aov(value ~ pos, data2lg)
summary(data2lg_aov)

## multi-compare

LSD.test(data2lg_aov, "pos", group = FALSE, console = TRUE)

## res
data2lg_res <- residuals(data2lg_aov)
data2lg_res

## model adequacy

windows()
setwd("D:\\GoogleDrive\\05 r\\Code(first 6 chapters)for Douglas-C.-Montgomery-Design-and-Analysis-of-Expe_2")
source("Chapter3/PP_plot.R")
pp.plot(data2lg_res, pch = 10, lty = 1, xlab = "Residual", line.method = "Q", legend.add = FALSE)

plot(data2lg_res ~ data2lg$value, pch = 22, xlab = "Tensile Strength", ylab = "Residuals")
abline(h = 0)

plot(data2lg_res ~ data2lg_aov$fitted.values, pch = 22, xlab = "Tensile Strength", ylab = "Residuals")
abline(h = 0)

shapiro.test(data2lg_res)
bartlett.test(data2lg$value ~ data2lg$pos, data = data2lg)
