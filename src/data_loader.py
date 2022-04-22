from torch.utils.data import DataLoader, random_split
from torchvision.datasets import ImageFolder

IMAGE_FOLDER_PATH = r'C:\Users\Selen\Desktop\tum-ai\data'

def get_dataloader(path, batch_size):
    # read the image data
    dataset = ImageFolder(path)

    # specify the train, valid and test dataset sizes
    train_valid_size = int(len(dataset) * 0.8)
    test_size = len(dataset) - train_valid_size
    valid_size = int(train_valid_size * 0.2)
    train_size = train_valid_size - valid_size

    # split the dataset into train, valid and test
    train_valid_set, test_set = random_split(dataset, [train_valid_size, test_size])
    train_set, valid_set = random_split(train_valid_set, [train_size, valid_size])

    # create dataloader for train, valid and test
    dataloader_train = DataLoader(train_set, batch_size, shuffle=True)
    dataloader_valid = DataLoader(valid_set, batch_size, shuffle=True)
    dataloader_test = DataLoader(test_set, batch_size, shuffle=True)

    return dataloader_train, dataloader_valid, dataloader_test
