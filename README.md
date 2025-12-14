# Text-To-QR-Code-Generator
A simple Flask web application that generates QR codes from user-provided text or URLs and allows users to download them instantly. The app is built using Python and Flask, and is deployed on PythonAnywhere for easy online access.


 📌 Flask QR Code Generator

A simple and lightweight **Flask web application** that generates **QR codes** from user-provided text and allows users to download them instantly.

🔗 **Live Demo:**
[https://amirqr.pythonanywhere.com/](https://amirqr.pythonanywhere.com/)


🚀 Features

* Generate QR codes from any text or URL
* Instant QR code preview and download
* Simple and clean user interface
* Built using Flask and Python
* Deployed on **PythonAnywhere**


 🛠️ Technologies Used

* **Python 3**
* **Flask**
* **qrcode library**
* **HTML / CSS**
* **PythonAnywhere** (Deployment)

📂 Project Structure

```
project/
│── app.py
│── templates/
│   └── index.html
│── qrcodes/
│   └── qrcode.png
│── requirements.txt
│── README.md
```

---

⚙️ Installation & Setup (Local)

1. Clone the repository

```bash
git clone https://github.com/AmirSohel2023/Text-To-QR-Code-Generator.git
```

2. Navigate to the project folder

```bash
cd flask-qrcode-generator
```

3. Create virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
pip install flask qrcode
pip install pillow
```

5. Run the application

```bash
python .\app.py
```



 🧪 How It Works

1. User enters text or URL
2. Flask receives form data via POST request
3. `qrcode` library generates a QR image
4. Image is saved and sent back to the user for download



🌍 Deployment

This project is deployed on **PythonAnywhere**, making it accessible online without local setup.


👤 Author

**Amir Sohel Sarkar Masum**

* GitHub: https://github.com/AmirSohel2023/Text-To-QR-Code-Generator
* Live Project: [https://amirqr.pythonanywhere.com/](https://amirqr.pythonanywhere.com/)


📄 License

This project is open-source and free to use for learning purposes.

