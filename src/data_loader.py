from torch.utils.data import DataLoader, random_split
import torch


def get_dataloader(dataset, batch_size):

    # set the seed
    torch.manual_seed(473)

    # initialize the dataloaders as empty dict
    dataloaders = {}

    # specify the train, valid and test dataset sizes
    train_valid_size = int(len(dataset) * 0.8)
    test_size = len(dataset) - train_valid_size
    valid_size = int(train_valid_size * 0.2)
    train_size = train_valid_size - valid_size

    # split the dataset into train, valid and test
    train_valid_set, test_set = random_split(dataset, [train_valid_size, test_size])
    train_set, valid_set = random_split(train_valid_set, [train_size, valid_size])

    # create dataloader for train, valid and test
    dataloaders['train'] = DataLoader(train_set, batch_size, shuffle=True, drop_last=True)
    dataloaders['val'] = DataLoader(valid_set, batch_size, shuffle=True, drop_last=True)
    dataloaders['test'] = DataLoader(test_set, batch_size, shuffle=True, drop_last=True)

    return dataloaders
