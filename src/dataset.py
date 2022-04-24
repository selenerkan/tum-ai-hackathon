import torch
from torch.utils.data import Dataset
from torchvision import transforms
import pandas as pd
import os

from PIL import Image


class XrayDataset(Dataset):
    def __init__(self, root, csv_path, transform=None):
        super(Dataset, self).__init__()

        if transform is None:
            self.transform = transforms.Compose([
                transforms.PILToTensor(),
                transforms.Resize(224),
            ])
        else:
            self.transform = transform

        self.root = root
        csv_df = pd.read_csv(csv_path, sep=';')
        csv_df = csv_df[['Image_Index', 'Finding_Labels']]
        csv_df['factorized_labels'], self.label_mapping = csv_df['Finding_Labels'].factorize()
        self.paths = csv_df['Image_Index'].tolist()
        self.labels = csv_df['factorized_labels'].tolist()

    def _loader(self, path):
        return Image.open(path).convert('RGB')

    def normalize(self, img):
        # Check that images are 2D arrays with 1 channel
        if img.shape != torch.Size([3, 224, 224]):
            img = img[0:3, :, :]
        if img.shape != torch.Size([3, 224, 224]):
            img = img.unsqueeze(0)
        assert(img.shape == torch.Size([3, 224, 224])), img.shape
        if len(img.shape) < 2:
            print("error, dimension lower than 2 for image")

        return ((2.0 * img / 255.0) - 1.0) * 1024

    def __getitem__(self, index):
        path = os.path.join(self.root, self.paths[index])
        img = self._loader(path)
        target = self.labels[index]

        img = self.transform(img)
        img = self.normalize(img)

        return img, target

    def __len__(self):
        return len(self.labels)
