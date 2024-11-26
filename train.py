import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from dataset import GoProDataset
from models.generator import Generator
from tqdm import tqdm
import os
from torchvision import transforms

# Modeli eğitme fonksiyonu
def train():
    # Veri setinin doğru yolu belirtildi
    transform = transforms.Compose([
        transforms.ToTensor(),  # Görüntüleri tensor'a dönüştür
    ])

    # En küçük batch_size ve veri seti yolu
    train_dataset = GoProDataset(data_dir="GOPRO_Large/train", transform=transform)
    train_loader = DataLoader(train_dataset, batch_size=1, shuffle=True, num_workers=0)

    # Modeli başlat
    model = Generator()  # Burada Generator sınıfını kullanıyoruz
    optimizer = optim.Adam(model.parameters(), lr=0.0002)

    # Eğitim döngüsü, sadece 1 epoch çalıştırılacak
    num_epochs = 1
    for epoch in range(num_epochs):
        model.train()
        pbar = tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs}", ncols=100)
        
        for images in pbar:
            # İleriye doğru geçiş ve kayıpları hesaplama
            blurred_images, sharp_images = images  # Burada veri çiftlerini aldığınızı varsayıyoruz
            optimizer.zero_grad()
            output_images = model(blurred_images)
            loss = torch.nn.functional.mse_loss(output_images, sharp_images)  # Kayıp fonksiyonu
            loss.backward()
            optimizer.step()
            
            pbar.set_postfix(loss=loss.item())
        
        # Modeli kaydet
        if not os.path.exists('models'):
            os.makedirs('models')  # Eğer 'models' klasörü yoksa oluştur
        torch.save(model.state_dict(), "models/generator.pth")  # Modelin ağırlıklarını kaydet

if __name__ == "__main__":
    train()
