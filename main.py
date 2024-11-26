import tkinter as tk
from tkinter import filedialog, Label, Button, messagebox
from PIL import Image
import os
import torch
from torchvision import transforms
from deblurgan import load_model

# Modeli yükleme
model = load_model("models/generator.pth")
model.eval()

# Çıktı klasörünü kontrol et ve oluştur
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Görüntüyü netleştirme işlemi
def deblur_image(input_image_path, output_image_path="output/deblurred_image.jpg"):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    
    # Görüntüyü yükle ve işleme
    image = Image.open(input_image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)  # Batch boyutunu ekle
    with torch.no_grad():
        output_tensor = model(input_tensor)
    
    # Çıktıyı tekrar görüntü formatına çevir
    output_image = output_tensor.squeeze(0).clamp(0, 1)  # Batch boyutunu kaldır
    output_image = transforms.ToPILImage()(output_image)
    
    # Görüntüyü kaydet
    output_image.save(output_image_path)
    return output_image_path

# Görüntüyü yükleme ve işleme
def load_and_process_image():
    input_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    if input_path:
        # Görüntüyü netleştir
        output_image_path = deblur_image(input_path)
        
        # Kullanıcıya bilgi mesajı göster
        messagebox.showinfo(
            "Processing Complete",
            f"Your image has been deblurred and saved to:\n{output_image_path}\n\n"
            "To process another image, please click 'Load Image' again."
        )

# Tkinter arayüzü
root = tk.Tk()
root.title("DeblurGAN v2 - Image Deblurring")

# Başlık
title_label = Label(root, text="DeblurGAN v2 - Image Deblurring Tool", font=("Arial", 16))
title_label.pack(pady=10)

# Görüntü yükleme düğmesi
load_button = Button(root, text="Load Image", command=load_and_process_image, font=("Arial", 12))
load_button.pack(pady=20)

# Tkinter döngüsü
root.mainloop()
