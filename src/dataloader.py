from torch.utils.data import Dataset
from torchvision import transforms
import pandas as pd
import os

from PIL import Image


class XrayDataset(Dataset):
    def __init__(self, root, csv_path, transform=None, target_transform=None):
        super(Dataset, self).__init__()

        if transform is None:
            self.transform = transforms.PILToTensor()
        else:
            self.transform = transform

        self.target_transform = target_transform

        self.root = root
        self.csv_df = pd.read_csv(csv_path, sep=';')
        self.csv_df = self.csv_df[['Image_Index', 'Finding_Labels']]
        self.csv_df['factorized_labels'], self.label_mapping = self.csv_df['Finding_Labels'].factorize()

    def _loader(self, path):
        return Image.open(path).convert('RGB')

    def __getitem__(self, index):
        path = os.path.join(self.root, self.csv_df['Image_Index'].iloc[index])
        print(path)
        img = self._loader(path)
        target = self.csv_df['factorized_labels'].iloc[index]

        if self.transform is not None:
            img = self.transform(img)
        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        return self.csv_df.size
