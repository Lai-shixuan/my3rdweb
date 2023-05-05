a <- c(1, 2, 3, 4, 5, 6)
a <- factor(a)

class(list1)
str(list1)
attributes(list1)

str(a)
b <- a
c <- list(a, b)

frame <- data.frame(a = c("a","b","c","d"), b = c(2,3,4,5))
str(frame)
list1 <- list(a = (frame$a), b = (frame$b))

windows()
plot(1, 1)

frame <- data.frame(list)

?tapply
as.factor(list1)
