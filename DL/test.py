import torch

x = torch.randn(9, 3)
y = x.repeat(1, 2)
z = y.view(9, 2, 3)
zx = z.permute(1, 0, 2)
zy = zx[0, :]
zz = zx[0]
zzx = zz[:-1]
# y = x[0, :]
