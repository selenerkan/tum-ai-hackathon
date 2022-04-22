import torch
import torchvision

from dataloader import XrayDataset

PATH = '../../data/'
CSV_FILE_PATH = '../Dataset_Chest_X_Ray_Sample.csv'

data_loader = XrayDataset(PATH, CSV_FILE_PATH)

model = torchvision.models.ResNet50(pretrained=True)

# Replace the last layer
model.fc = torch.nn.Linear(2048, 15)


# Training loop for ResNet50
def train(model, train_loader, optimizer, criterion, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data, target
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.item()))
