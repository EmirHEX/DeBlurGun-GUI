from dataset import GoProDataset
from torch.utils.data import DataLoader

dataset = GoProDataset(split="test")
data_loader = DataLoader(dataset, batch_size=8, shuffle=True)

for blur_images, sharp_images in data_loader:
    print(f"Bulanık: {blur_images.shape}, Keskin: {sharp_images.shape}")
    break
