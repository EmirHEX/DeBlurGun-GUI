import torch
import os
from models.generator import Generator

def load_model(model_path="models/generator.pth"):
    if os.path.exists(model_path):
        model = Generator()
        model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        model.eval()  # Modeli eval modunda kullan
        print(f"Model başarıyla yüklendi: {model_path}")
        return model
    else:
        raise FileNotFoundError(f"Model dosyası bulunamadı: {model_path}")
