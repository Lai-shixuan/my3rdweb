#%%
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torch.optim import Adam
from sklearn.model_selection import KFold
from sklearn.datasets import make_classification

#%%
# 定义一个简单的二分类模型
class SimpleClassifier(nn.Module):
    def __init__(self):
        super(SimpleClassifier, self).__init__()
        self.fc = nn.Linear(20, 2)

    def forward(self, x):
        return self.fc(x)

#%%
# 创建一个模拟数据集
X, y = make_classification(n_samples=100, n_features=20, n_informative=20, n_redundant=0, random_state=42)
X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.long)

# 定义损失函数
criterion = nn.CrossEntropyLoss()

# 5-fold cross validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

#%%

for i in enumerate(kfold.split(X)):
    print(i)

#%%
for fold, (train_ids, test_ids) in enumerate(kfold.split(X)):
    print(f'FOLD {fold}')
    print('--------------------------------')

    # 定义模型和优化器
    model = SimpleClassifier()
    optimizer = Adam(model.parameters(), lr=0.001)

    # 划分训练集和验证集
    X_train, X_test = X[train_ids], X[test_ids]
    y_train, y_test = y[train_ids], y[test_ids]

    # 创建 DataLoader
    train_dataset = TensorDataset(X_train, y_train)
    test_dataset = TensorDataset(X_test, y_test)
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=16)

    # 模型训练
    for epoch in range(10):  # 在实际应用中，你可能需要更多的epoch
        for inputs, targets in train_loader:
            optimizer.zero_grad()

            # 前向传播
            outputs = model(inputs)
            loss = criterion(outputs, targets)

            # 后向传播和优化
            loss.backward()
            optimizer.step()

        # 输出loss
        if (epoch+1) % 5 == 0:
            print (f'Epoch [{epoch+1}/10], Loss: {loss.item()}')

    # 验证模型
    model.eval()
    total = 0
    correct = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = correct / total
    print(f'Accuracy of the model on the test set: {accuracy * 100} %')