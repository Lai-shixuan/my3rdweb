import torch
from torcheval.metrics import R2Score

metric = R2Score()
input = torch.tensor([1.2, 2.5, 3.6, 4.5, 6])
target = torch.tensor([1, 2, 3, 4, -5])
metric.update(input, target)
a = metric.compute()
