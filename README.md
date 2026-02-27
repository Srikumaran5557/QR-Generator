Perfect — below is a **complete GitHub-ready README.md** with everything expected in a polished repo:

* Overview
* Features
* Screenshots
* Installation
* Usage
* QR formats
* AppImage
* Dependencies
* Structure
* Tech stack
* Packaging
* Author
* License
* Contributing

You can paste this directly into **README.md**.

---

# 📱 QR Utility Desktop

Multi-format QR code desktop application supporting **Text, WiFi, Contact, UPI, and Location (DMS)** with **PNG/SVG export** and a modern **ttkbootstrap UI**.
Packaged for Linux as a portable **AppImage**.

---

## ✨ Features

* Generate QR codes for:

  * 🔗 Text / URL
  * 📶 WiFi credentials
  * 👤 Contact (vCard)
  * 💳 UPI payment
  * 📍 Location (DMS → Google Maps pin)
* Export as **PNG** and **SVG**
* Accurate **Google Maps location QR**
* Clean **tabbed desktop UI**
* Input validation
* Cross-platform Python app
* Linux **AppImage** distribution

---

## 🖼️ Screenshots

> Place images inside `Screenshots/`

| Main Window                   | Tabs                          |
| ----------------------------- | ----------------------------- |
| ![Main](Screenshots/main.png) | ![Tabs](Screenshots/tabs.png) |

---

## 📂 Project Structure

```
QR-Generator/
│
├── qr_app.py
├── requirements.txt
├── README.md
├── .gitignore
├── icon.png
└── Screenshots/
    ├── main.png
    └── tabs.png
```

---

## ⚙️ Requirements

* Python ≥ 3.9
* Tkinter (system package)

### Python dependencies

```
ttkbootstrap>=1.10
qrcode[svg]>=7.4
Pillow>=10.0
```

### System dependency (Linux)

```
sudo apt install python3-tk
```

---

## 🚀 Installation

### 1️⃣ Clone repository

```
git clone https://github.com/Srikumaran5557/QR-Generator.git
cd QR-Generator
```

### 2️⃣ Create virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run application

```
python qr_app.py
```

---

## 🧭 Usage

1. Select QR type tab
2. Enter required data
3. Click **Generate**
4. Save as PNG or SVG

---

## 📍 Location QR (DMS)

Accepts coordinates like:

```
12°14'27.7"N 79°03'26.1"E
```

Automatically converts to decimal and generates a precise Google Maps QR.

---

## 💳 UPI QR

Generates standard payment payload:

```
upi://pay?pa=<UPI_ID>&pn=<NAME>&am=<AMOUNT>&cu=INR
```

Compatible with:

* Google Pay
* PhonePe
* Paytm
* BHIM

---

## 📶 WiFi QR

```
WIFI:T:<ENC>;S:<SSID>;P:<PASSWORD>;;
```

---

## 👤 Contact QR (vCard)

```
BEGIN:VCARD
VERSION:3.0
FN:<NAME>
TEL:<PHONE>
EMAIL:<EMAIL>
END:VCARD
```

---

## 🖨️ Export Formats

* **PNG** → sharing & screens
* **SVG** → print & vector graphics

---

## 🐧 AppImage (Linux)

Portable standalone build:

```
QRUtility-x86_64.AppImage
```

Run:

```
chmod +x QRUtility-x86_64.AppImage
./QRUtility-x86_64.AppImage
```

No Python required.

---

## 🧱 Tech Stack

* Python
* Tkinter
* ttkbootstrap
* qrcode
* Pillow
* PyInstaller
* AppImage

---

## 📦 Packaging

Build pipeline:

```
qr_app.py
   ↓ PyInstaller
dist/qr_app
   ↓ AppDir
QRUtility.AppDir
   ↓ appimagetool
QRUtility-x86_64.AppImage
```

---

## 🧪 Validation

* UPI format validation
* Numeric amount check
* DMS coordinate parsing
* Latitude/Longitude range checks

---

## 👨‍💻 Author

**Srikumaran S.S.**
B.Tech Electrical & Electronics Engineering
NIT Trichy

GitHub: [https://github.com/Srikumaran5557](https://github.com/Srikumaran5557)

---

## 📄 License

MIT License

---

## 🤝 Contributing

Contributions are welcome.

1. Fork repository
2. Create feature branch
3. Commit changes
4. Open Pull Request

---

## ⭐ Acknowledgements

* ttkbootstrap
* qrcode
* Pillow
* Tkinter

---

# ✔️ What you should do now

1. Copy this into `README.md`
2. Ensure screenshots exist:

```
Screenshots/main.png
Screenshots/tabs.png
```

3. Commit & push:

```
git add README.md
git commit -m "Add complete project README"
git push
```

---

If you want, I can also provide:

* MIT LICENSE file
* GitHub release text
* AppImage build instructions section
* README badges

Just tell me.
