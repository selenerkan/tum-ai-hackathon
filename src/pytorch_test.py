import torch
import torchvision
import torchxrayvision as xrv

from dataset import XrayDataset
from data_loader import get_dataloader

PATH = '../../data/images_sample'
CSV_FILE_PATH = '../Dataset_Chest_X_Ray_Sample.csv'

dataset = XrayDataset(PATH, CSV_FILE_PATH)
dataloaders = get_dataloader(dataset, batch_size=4)

for i, (images, labels) in enumerate(dataloaders['train']):
    print(i)
    print(images.shape)
    print(labels.shape)
    break


model = xrv.models.DenseNet(weights="densenet121-res224-nih")

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

def evaluate(model, val_loader, criterion):
    model.eval()
    val_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in val_loader:
            output = model(data)
            val_loss += criterion(output, target).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
    val_loss /= len(val_loader.dataset)
    print('\nValidation set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        val_loss, correct, len(val_loader.dataset),
        100. * correct / len(val_loader.dataset)))


if __name__ == '__main__':
    # for epoch in range(1, 10):
    #     train(model, dataloaders['train'], optimizer, criterion, epoch)

    evaluate(model, dataloaders['val'], criterion)
