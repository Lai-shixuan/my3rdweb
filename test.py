import torch
import a

if torch.cuda.is_available():
    print(True)

label_dict = {'a', 'b', 'c'}

a.print_abc()

abc = ()

# %%
import os

for i in os.getenv('PYTHONPATH').split(os.pathsep):
    print(i)

# %%
print(f"Hello, {input('Name:')}")


# %%
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")

    return wrapper


@announce
def hello():
    print("Hello, world!")


hello()

#%%
import torch
import pandas as pd

pt1 = torch.load("DL/hw2/data/libriphone/libriphone/feat/train/19-198-0008.pt")
pt2 = torch.load("DL/hw2/data/libriphone/libriphone/feat/test/19-198-0037.pt")
doc1 = pd.read_csv("DL/hw2/data/libriphone/libriphone/train_labels.csv")
