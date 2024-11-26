from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import os

class GoProDataset(Dataset):
    def __init__(self, data_dir, transform=None, max_samples=10):  # max_samples parametresi eklendi
        self.data_dir = data_dir
        self.transform = transform
        self.max_samples = max_samples  # Maksimum örnek sayısı

        self.blur_images = []
        self.sharp_images = []

        # Verinin yolunu gez
        for subdir in os.listdir(self.data_dir):
            blur_dir = os.path.join(self.data_dir, subdir, 'blur')
            sharp_dir = os.path.join(self.data_dir, subdir, 'sharp')

            if os.path.exists(blur_dir) and os.path.exists(sharp_dir):
                blur_images = sorted(os.listdir(blur_dir))
                sharp_images = sorted(os.listdir(sharp_dir))

                self.blur_images += [os.path.join(blur_dir, image) for image in blur_images]
                self.sharp_images += [os.path.join(sharp_dir, image) for image in sharp_images]

        # Sadece max_samples kadar örnek al
        self.blur_images = self.blur_images[:self.max_samples]
        self.sharp_images = self.sharp_images[:self.max_samples]

    def __len__(self):
        return len(self.blur_images)

    def __getitem__(self, idx):
        blur_image = Image.open(self.blur_images[idx]).convert("RGB")
        sharp_image = Image.open(self.sharp_images[idx]).convert("RGB")

        if self.transform:
            blur_image = self.transform(blur_image)
            sharp_image = self.transform(sharp_image)

        return blur_image, sharp_image
