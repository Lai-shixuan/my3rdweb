library(reshape2)
data1 <- matrix(c(73, 68, 74, 71, 67, 73, 67, 75, 72, 70, 75, 68, 78, 73, 68, 73, 71, 75, 75, 69), nrow = 4, byrow=TRUE)
colnames(data1) <- LETTERS[1:5] # 表列命名
rownames(data1) <- c("CH1", "CH2", "CH3", "CH4")  # 表行命名
head(data1)
data_final <- melt(data1) # 将ABCDE均设为变量进行展开
head(data_final)
data_final.aov <- aov(value ~ factor(Var1) + factor(Var2), data_final)  # 设置VAR1和VAR2列都是变量，其中VAR1列是处理，VAR2是区组
summary(data_final.aov)

# # 对组1和组4进行t检验
# data2 <- data1[1,]-data1[4,]
# t.test(x = data2, mu = 0, var.equal = FALSE, conf.level = 0.95)
#
# # 对组1和组4进行方差检验
# datatemp <- rbind(data1[1,], data1[4, ])
# datatemp_final <- melt(datatemp) # 将ABCDE均设为变量进行展开
# datatemp_final.aov <- aov(value ~ Var1 + Var2, datatemp_final)  # 设置VAR1和VAR2列都是变量，其中VAR1列是处理，VAR2是区组
# summary(datatemp_final.aov)

# 正态假设
setwd("D:\\GoogleDrive\\05 r\\Code(first 6 chapters)for Douglas-C.-Montgomery-Design-and-Analysis-of-Expe_2")
source("Chapter3/PP_plot.R")
windows()
data_final_res <- residuals(data_final.aov)
pp.plot(data_final_res, pch = 10, lty = 1, xlab = "Residual", line.method = "Q", legend.add = FALSE)

shapiro.test(data_final_res)

# 残差随预测压强的分布图
plot(data_final_res ~ data_final.aov$fitted.values, pch = 22, xlab = "Tensile Strength", ylab = "Residuals")
abline(h = 0)

# 残差随实值的变化
windows()
plot(data_final_res ~ data_final$value, pch = 22, xlab = "Tensile Strength", ylab = "Residuals")
abline(h = 0)

#  方差齐性
# 错误，应该不允许在互有干扰因素的时候，抽出1个因子来检验
# bartlett.test(data_final$value ~ data_final$Var1, data = data_final)