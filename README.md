# 📱 QR Utility Desktop

Multi-format QR code desktop application supporting **Text, WiFi, Contact, UPI, and Location (DMS)** with **PNG/SVG export** and a modern **ttkbootstrap UI**.

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


## 🧱 Tech Stack

* Python
* Tkinter
* ttkbootstrap
* qrcode
* Pillow

---

