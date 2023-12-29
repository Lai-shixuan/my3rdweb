import numpy as np

a = np.arange(6).reshape(6, )
print(a)
# [[0 1 2]
#  [3 4 5]]

print(a.shape)
a = a[:, None]
# (2, 3)a = np.arange(6).reshape(2, 3)
# print(a)
# # [[0 1 2]
# #  [3 4 5]]
#
# print(a.shape)
# # (2, 3)