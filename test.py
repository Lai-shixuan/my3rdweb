import torch
import a

if torch.cuda.is_available():
    print(True)

label_dict = {'a', 'b', 'c'}

a.print_abc()

abc = ()


#%%
import os
for i in os.getenv('PYTHONPATH').split(os.pathsep):
    print(i)

#%%
