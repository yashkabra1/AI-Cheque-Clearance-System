# 🏦 AI Cheque Clearance System

> An AI-powered cheque processing system that automatically detects cheque fields, extracts information using Google Gemini Vision, verifies customer details from a MySQL database, and decides whether a cheque should be approved or rejected.

---

## 📌 Project Overview

Manual cheque verification is time-consuming and prone to human error.

This project automates the entire cheque clearance process using Artificial Intelligence and Computer Vision.

The system performs:

- Cheque field detection using YOLOv8
- OCR using Google Gemini Vision
- Customer verification using MySQL
- Balance verification
- MICR verification
- Transaction logging
- Automatic cheque approval/rejection
- Excel report generation

---

## ✨ Features

✅ Automatic Cheque Field Detection

✅ Google Gemini Vision OCR

✅ Customer Verification

✅ Account Verification

✅ MICR Verification

✅ Balance Verification

✅ Transaction Logging

✅ Excel Report Generation

✅ MySQL Database Integration

✅ Modular Python Architecture

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| YOLOv8 | Cheque Field Detection |
| Google Gemini Vision | OCR |
| OpenCV | Image Processing |
| SQLAlchemy | ORM |
| MySQL | Database |
| Pandas | Report Generation |
| Git | Version Control |
| GitHub | Repository |

---

## 📂 Project Structure

```text
AI-Cheque-Clearance-System
│
├── database
│   ├── connection.py
│   ├── models.py
│   ├── queries.py
│   ├── Create_Tables.py
│   └── insert_sample_data.py
│
├── dataset
│   ├── Images
│   ├── train
│   ├── valid
│   └── data.yaml
│
├── services
│   ├── decision_engine.py
│   ├── verification.py
│   └── utils.py
│
├── runs
│   └── detect
│       └── train4
│           └── weights
│               └── best.pt
│
├── reports
│
├── Cropped_Fields
│
├── cheque_reader.py
├── gemini_client.py
├── ocr_utils.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yashkabra1/AI-Cheque-Clearance-System.git

cd AI-Cheque-Clearance-System
```

---

### Create a Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a file named

```text
.env
```

Copy the contents from

```text
.env.example
```

Example:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=ai_cheque_clearance
```

---

## 🗄️ Create Database Tables

Run:

```bash
python database/Create_Tables.py
```

---

## 📥 Insert Sample Data

```bash
python database/insert_sample_data.py
```

---

## 🚀 Run the Project

```bash
python cheque_reader.py
```

---

## 📊 Output

After successful execution the project automatically generates:

- Cropped cheque fields
- Extracted cheque information
- MySQL transaction records
- Verification results
- Excel report

The generated report will be available inside:

```text
reports/
```

---
