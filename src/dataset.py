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
                transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
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

    def __getitem__(self, index):
        path = os.path.join(self.root, self.paths[index])
        print(path)
        img = self._loader(path)
        target = self.labels[index]

        if self.transform is not None:
            img = self.transform(img)
        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        return len(self.labels)
