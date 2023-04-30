class ABC:
    size = 0


c1 = ABC()
c2 = c1

c1.size = 10
print(c2.size)

c1 = 1
print(c1)