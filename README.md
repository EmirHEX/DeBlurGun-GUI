DeblurGAN v2 - Academic Project
🎓 A Student-Friendly Implementation of Image Deblurring with DeblurGAN v2

This project is an educational implementation of DeblurGAN v2, designed for university students and researchers interested in image processing, deep learning, and GAN-based architectures. It includes simplified training and testing pipelines for learning and experimenting with deblurring techniques on images.

🔍 Overview
DeblurGAN v2 is a Generative Adversarial Network (GAN) designed to restore sharpness in blurry images. This project demonstrates its use on the GoPro Large Dataset with the following simplified workflow:

Load a blurry image.
Use a pre-trained generator model to restore the sharp image.
Save and display the processed image for evaluation.
Key Features:
Student-Centric Design: Built with simplicity to help students learn the fundamentals of GANs and image deblurring.
Pre-Trained Model Included: A pre-trained model is provided for immediate testing.
Custom Training Support: Includes a training script for experimenting with the GoPro dataset.
Tkinter GUI: A simple interface for loading and processing images.
Minimal Dependencies: Lightweight implementation for ease of use.
📚 Technical Background
What is DeblurGAN v2?
DeblurGAN v2 is a GAN architecture tailored for the task of image deblurring. Unlike traditional deblurring methods, it employs:

Generator Network: To predict sharp images from blurry inputs.
Discriminator Network: To distinguish between real and generated sharp images.
Perceptual Loss Function: To preserve image features during deblurring.
How Does It Work?
Input: A blurry image (e.g., motion blur or out-of-focus images).
Transformation: The generator network applies learned transformations to the image.
Output: A sharp image, visually close to the original unblurred photo.
Why Use GANs?
GANs are capable of learning complex mappings between input and output domains, making them ideal for tasks like deblurring, super-resolution, and image-to-image translation.

📂 Project Structure
plaintext
Kodu kopyala
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
🚀 Getting Started
1. Installation
Prerequisites:
Python 3.8 or later
pip (Python package manager)
Steps:
Clone the repository:
bash
Kodu kopyala
git clone https://github.com/YOUR_USERNAME/DeblurGANv2-StudentProject.git
cd DeblurGANv2-StudentProject
Install dependencies:
bash
Kodu kopyala
pip install -r requirements.txt
2. Usage
Training the Model:
Make sure the GoPro Large Dataset is correctly organized:
bash
Kodu kopyala
GOPRO_Large/
├── train/
├── test/
Run the training script:
bash
Kodu kopyala
python train.py
Testing with GUI:
Start the GUI by running:
bash
Kodu kopyala
python main.py
Click "Load Image" to select a blurry image. The processed sharp image will be saved in the output/ folder.
🔧 How It Works
Dataset Preprocessing: The dataset is preprocessed into tensor batches, resized, and normalized.
Training Pipeline: The generator learns to minimize the perceptual loss while the discriminator ensures realistic results.
Inference: The pre-trained model restores sharpness to blurry inputs by mapping the blurry images to the sharp domain.
👩‍💻 For Students
This project demonstrates key concepts in:

Generative Adversarial Networks (GANs): Understanding generator-discriminator interplay.
Image Processing: Restoration of degraded images using neural networks.
Deep Learning Training: Customizing loss functions and optimizers for specific tasks.
Python GUI Development: Using Tkinter to create interactive tools.
💡 Contribution
This project is open to contributions for improving its functionality or extending its scope. Feel free to fork and submit a pull request!

📜 License
This project is for educational purposes only and uses parts of the DeblurGAN v2 architecture.

