import torch
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()

        # İlk konvolüsyonel katman (3 kanal, 64 kanal çıkış)
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
        
        # İkinci konvolüsyonel katman (64 kanal, 3 kanal çıkış)
        self.conv2 = nn.Conv2d(64, 3, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        """
        Bu fonksiyon modelin nasıl çalışacağını tanımlar.
        x: Girdi bulanık görüntü
        """
        x = self.conv1(x)  # İlk konvolüsyon katmanı
        x = torch.relu(x)  # ReLU aktivasyon fonksiyonu
        x = self.conv2(x)  # İkinci konvolüsyon katmanı
        return x  # Çıktı: Keskinleştirilmiş görüntü
