# **DeblurGAN v2 - Academic Project**

🎓 **A Student-Friendly Implementation of Image Deblurring with DeblurGAN v2**

This project is an **educational implementation** of **DeblurGAN v2**, designed for university students and researchers interested in **image processing**, **deep learning**, and **GAN-based architectures**. It includes simplified training and testing pipelines for learning and experimenting with deblurring techniques on images.

---

## **🔍 Overview**

DeblurGAN v2 is a **Generative Adversarial Network (GAN)** designed to restore sharpness in blurry images. This project demonstrates its use on the **GoPro Large Dataset** with the following simplified workflow:

1. Load a blurry image.
2. Use a pre-trained generator model to restore the sharp image.
3. Save and display the processed image for evaluation.

### **Key Features:**

- **Student-Centric Design:** Built with simplicity to help students learn the fundamentals of GANs and image deblurring.
- **Pre-Trained Model Included:** A pre-trained model is provided for immediate testing.
- **Custom Training Support:** Includes a training script for experimenting with the GoPro dataset.
- **Tkinter GUI:** A simple interface for loading and processing images.
- **Minimal Dependencies:** Lightweight implementation for ease of use.

---

## **📚 Technical Background**

### **What is DeblurGAN v2?**

DeblurGAN v2 is a **GAN architecture** tailored for the task of **image deblurring**. Unlike traditional deblurring methods, it employs:

1. **Generator Network:** To predict sharp images from blurry inputs.
2. **Discriminator Network:** To distinguish between real and generated sharp images.
3. **Perceptual Loss Function:** To preserve image features during deblurring.

### **How Does It Work?**

1. **Input:** A blurry image (e.g., motion blur or out-of-focus images).
2. **Transformation:** The generator network applies learned transformations to the image.
3. **Output:** A sharp image, visually close to the original unblurred photo.

---

## **📂 Project Structure**

```plaintext
DeblurGANv2-StudentProject/
│
├── main.py               # GUI for testing deblurring on custom images.
├── deblurgan.py          # Functions for loading the model and deblurring images.
├── train.py              # Training loop for the generator network.
├── dataset.py            # Dataset loader for GoPro Large Dataset.
├── models/               # Contains the pre-trained generator model.
│   └── generator.pth     # Pre-trained model file.
├── output/               # Directory for saving processed images.
│   └── deblurred_image.jpg # Example deblurred output.
├── logs/                 # Logs for training progress.
│   └── train_log.txt     
├── resources/            # Example blurry image for testing.
│   └── sample_blur.jpg   
├── requirements.txt      # Dependencies required to run the project.
└── README.md             # Project documentation.
