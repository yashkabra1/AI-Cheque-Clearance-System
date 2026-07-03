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

# 🏗️ System Architecture

```text
                    ┌────────────────────┐
                    │   Cheque Image     │
                    └─────────┬──────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │     YOLOv8 Detection    │
                 └─────────┬──────────────┘
                           │
           Detects Account, Payee, Amount,
           Date, MICR, Signature, etc.
                           │
                           ▼
              ┌──────────────────────────┐
              │    Crop Each Field       │
              └─────────┬────────────────┘
                        │
                        ▼
              ┌──────────────────────────┐
              │  Google Gemini Vision    │
              │        OCR               │
              └─────────┬────────────────┘
                        │
                        ▼
             Structured Cheque Information
                        │
                        ▼
             ┌─────────────────────────┐
             │ Verification Engine     │
             └─────────┬───────────────┘
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
 Account Check    Balance Check    MICR Check
      │                │                │
      └────────────────┼────────────────┘
                       ▼
              ┌──────────────────────┐
              │   Decision Engine    │
              └─────────┬────────────┘
                        │
          ┌─────────────┴──────────────┐
          ▼                            ▼
      APPROVED                     REJECTED
          │
          ▼
   Update MySQL Database
          │
          ▼
 Generate Excel Report
```

---

# 🔄 Workflow

The complete workflow of the AI Cheque Clearance System is:

1. Upload a cheque image.
2. YOLOv8 detects cheque fields.
3. Each detected field is cropped.
4. Google Gemini Vision extracts text from each field.
5. Extracted data is converted into structured cheque information.
6. The Verification Engine validates:
   - Account Number
   - MICR Code
   - Account Status
   - Available Balance
   - Cheque Date
7. The Decision Engine decides whether the cheque should be approved or rejected.
8. Customer balance is updated if approved.
9. Transaction details are stored in the MySQL database.
10. A final Excel report is generated.

---

# 🧠 Verification Process

The system performs the following checks before approving a cheque:

- ✅ Customer Exists
- ✅ Account Number Exists
- ✅ MICR Code Matches
- ✅ Account is Active
- ✅ Available Balance is Sufficient
- ✅ Cheque Date is Valid
- ✅ Amount is Positive

If any validation fails, the cheque is rejected with a reason.

---

# 🗄️ Database Design

The project uses MySQL with SQLAlchemy ORM.

### Customers Table

| Column | Description |
|---------|-------------|
| customer_id | Customer ID |
| first_name | First Name |
| last_name | Last Name |
| account_number | Bank Account Number |
| micr | MICR Code |
| balance | Available Balance |
| account_status | Active / Inactive |

---

### Transactions Table

| Column | Description |
|---------|-------------|
| transaction_id | Transaction ID |
| customer_id | Customer ID |
| cheque_amount | Amount |
| status | Approved / Rejected |
| remarks | Decision Reason |
| created_at | Timestamp |

---

# 🎥 Project Demo

You can also include a short GIF demonstrating:

- Uploading a cheque image
- YOLO detecting fields
- Gemini extracting text
- Verification process
- Cheque approval/rejection
- Excel report generation

A short 20–30 second GIF provides a quick overview of the system without requiring users to run the project.

---

# 🚀 Future Enhancements

The following features are planned for future releases:

- ✅ AI Signature Verification
- ✅ Flask REST API
- ✅ React Dashboard
- ✅ User Authentication
- ✅ Docker Support
- ✅ Cloud Deployment (AWS / Azure)
- ✅ PDF Report Generation
- ✅ Email Notification System
- ✅ SMS Notification
- ✅ Cheque Fraud Detection
- ✅ Transaction History Dashboard
- ✅ Real-time Processing Queue

---

# 📈 Project Roadmap

| Feature | Status |
|----------|--------|
| YOLO Field Detection | ✅ Completed |
| Gemini Vision OCR | ✅ Completed |
| MySQL Database | ✅ Completed |
| SQLAlchemy ORM | ✅ Completed |
| Verification Engine | ✅ Completed |
| Decision Engine | ✅ Completed |
| Excel Report Generation | ✅ Completed |
| Signature Verification | 🚧 In Progress |
| Flask REST API | 📅 Planned |
| React Dashboard | 📅 Planned |
| Docker Deployment | 📅 Planned |
| Cloud Deployment | 📅 Planned |

---

# 💻 Technologies Used

### Artificial Intelligence

- YOLOv8
- Google Gemini Vision
- OpenCV

### Backend

- Python
- SQLAlchemy
- MySQL

### Data Processing

- Pandas
- NumPy

### Development Tools

- Git
- GitHub
- Visual Studio Code

---

# 📊 Sample Output

```text
========================================

AI CHEQUE CLEARANCE SYSTEM

========================================

Image :

Cheque001.jpg

Account :

1000000001

Payee :

Yash Kabra

Amount :

25000

MICR :

MICR000001

Verification :

✔ Account Verified

✔ Balance Verified

✔ MICR Verified

✔ Date Verified

✔ Account Active

----------------------------------------

STATUS :

APPROVED

Transaction ID :

1052

Remaining Balance :

₹225000

========================================
```

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve the project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

See the LICENSE file for more information.

---

# 👨‍💻 Author

**Yash Kabra**

BCA (Hons.) – Gaming & Animation

Artificial Intelligence • Computer Vision • Python Development

GitHub:

https://github.com/yashkabra1

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the following projects:

- Ultralytics YOLOv8
- Google Gemini
- OpenCV
- SQLAlchemy
- MySQL
- Pandas

---

# ⭐ If you like this project

If you found this project useful:

⭐ Star this repository

🍴 Fork the repository

📢 Share it with others

---

> **Built with ❤️ using Artificial Intelligence, Computer Vision, and Python**
