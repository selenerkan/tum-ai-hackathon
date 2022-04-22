import torch
import torchvision

from dataset import XrayDataset
from data_loader import get_dataloader

PATH = '../../data/images_sample'
CSV_FILE_PATH = '../Dataset_Chest_X_Ray_Sample.csv'

dataset = XrayDataset(PATH, CSV_FILE_PATH)
dataloaders = get_dataloader(dataset, batch_size=4)

model = torchvision.models.resnet50(pretrained=True)

for i, (images, labels) in enumerate(dataloaders['train']):
    print(i)
    print(images.shape)
    print(labels.shape)
    break

# Replace the last layer
model.fc = torch.nn.Linear(2048, 15)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

criterion = torch.nn.CrossEntropyLoss()

# Training loop for ResNet50
def train(model, train_loader, optimizer, criterion, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.item()))

if __name__== '__main__':
    for epoch in range(1, 10):
        train(model, dataloaders['train'], optimizer, criterion, epoch)
