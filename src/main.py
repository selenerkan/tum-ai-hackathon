import torch
import torchvision
from torchmetrics import MetricCollection, Accuracy, Precision, Recall
from tqdm import tqdm

from src.config import PATH, CSV_FILE_PATH, DEVICE, BATCH_SIZE, LEARNING_RATE, EPOCHS, CLASS_WEIGHTS
from dataset import XrayDataset
from data_loader import get_dataloader
from utils import freeze_model, new_classification_layer

# =============================================================================
# Dataset and dataloader
dataset = XrayDataset(PATH, CSV_FILE_PATH)
dataloaders = get_dataloader(dataset, batch_size=BATCH_SIZE)

# Model
model = torchvision.models.resnet50(pretrained=True).device(DEVICE)
freeze_model(model)
model = new_classification_layer(model, n_classes=15)

# Optimizer, loss function and metrics
optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
criterion = torch.nn.CrossEntropyLoss(weight=torch.tensor(CLASS_WEIGHTS))
metric_collection = MetricCollection([
    Accuracy(),
    Precision(num_classes=15, average='macro'),
    Recall(num_classes=15, average='macro')
])


# =============================================================================
# Training and evaluation functions
def train(model, train_loader, optimizer, criterion, epoch):
    print("Starting model training.")
    print(f"BATCH SIZE: {BATCH_SIZE}, len(train_loader): {len(train_loader)}, num_batches: {len(train_loader)//BATCH_SIZE}")
    model.train()
    for batch_idx, (data, target) in enumerate(tqdm(train_loader)):
        data, target = data.to(DEVICE), target.to(DEVICE)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.cpu().item()))


def evaluate(model, val_loader, criterion):
    print("Starting model evaluation.")
    print(f"BATCH SIZE: {BATCH_SIZE}, len(val_loader): {len(val_loader)}, num_batches: {len(val_loader)//BATCH_SIZE}")
    model.eval()
    val_loss = 0
    softmax = torch.nn.Softmax(dim=1)
    with torch.no_grad():
        for i, (data, target) in enumerate(tqdm(val_loader)):
            data, target = data.to(DEVICE), target.to(DEVICE)
            output = model(data)
            val_loss += criterion(output, target).cpu().item()
            metric_collection.update(softmax(output), target)
    val_loss /= len(val_loader.dataset)
    print('\nValidation set: Average loss: {:.4f}\n'.format(val_loss))
    print(metric_collection.compute())


# =============================================================================
# The main loop
if __name__ == '__main__':
    for epoch in range(EPOCHS):
        train(model, dataloaders['train'], optimizer, criterion, epoch)
        evaluate(model, dataloaders['val'], criterion)
