# Captcha-Generator
A CAPTCHA Generator in Python creates images with random text (letters/numbers) and distortion to differentiate humans from bots.

🔐 Python CAPTCHA Generator

A simple and customizable CAPTCHA Generator built using Python and the Pillow library. This project generates CAPTCHA images with random text, colors, and noise to simulate human verification systems used on websites.


📌 Features

- Random CAPTCHA text generation (letters + numbers)
- Image-based CAPTCHA output
- Noise addition (lines and dots)
- Blur effect for distortion
- Customizable length and styles
- Saves CAPTCHA as an image file


🛠️ Technologies Used

- Python 3.x
- Pillow (PIL - Python Imaging Library)


📦 Installation

1. Clone this repository:

git clone https://github.com/your-username/captcha-generator.git
cd captcha-generator

2. Install required dependencies:

pip install pillow


▶️ Usage

Run the Python script:

python captcha.py

After running:

- A CAPTCHA image will be displayed
- The image will be saved as "captcha.png"
- The CAPTCHA text will be printed in the console


🧠 How It Works

1. Generates a random string using letters and digits
2. Creates a blank image using Pillow
3. Draws each character with random color and position
4. Adds noise (lines and dots)
5. Applies blur filter for distortion
6. Saves and displays the CAPTCHA image


📁 Project Structure

captcha-generator/
│
├── captcha.py          # Main script
├── captcha.png         # Generated output
├── requirements.txt    # Dependencies
└── README.md           # Project documentation


⚙️ Configuration

You can modify:

- CAPTCHA length
- Image size
- Font style
- Noise level
- Colors


🚀 Future Improvements

- Add GUI using Tkinter
- Web integration using Flask/Django
- Audio CAPTCHA support
- Stronger distortion techniques
- CAPTCHA verification system


📜 License

This project is open-source and available under the MIT License.


🙌 Contribution

Contributions are welcome! Feel free to fork this repository and submit a pull request.


👨‍💻 Author

Shoheb Mulla 
GitHub: https://github.com/your-shoheb07
