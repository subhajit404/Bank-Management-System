# 🏦 Bank Management System

> **A simple, secure, and interactive banking system built with Python, JSON, and Streamlit.**

Managing a bank account shouldn't feel complicated.

This project brings essential banking operations into one clean web interface where users can **create accounts, deposit money, withdraw funds, view account details, update information, and delete accounts** — all powered by a Python backend and a lightweight JSON database.

---

## ✨ Why This Project?

This project was built to understand how real-world applications work behind the scenes.

Instead of keeping everything inside a single menu-driven Python program, the system separates:

* 🧠 **Banking logic** → Python OOP
* 💾 **Data storage** → JSON
* 🖥️ **User interface** → Streamlit
* 🔐 **Account verification** → Account number + PIN
* ⚡ **Application flow** → Interactive web interface

The result is a small but complete banking application that demonstrates the fundamentals of **backend logic, data persistence, validation, and UI development**.

---

## 🚀 Features

### 👤 Account Management

Create a new bank account with:

* Full name
* Age
* Email
* 4-digit PIN
* Automatically generated account number
* Initial balance of ₹0

### 💰 Deposit Money

Users can deposit money into their account.

The system validates:

* Account number
* PIN
* Positive deposit amount
* Maximum deposit limit of ₹10,000

### 💸 Withdraw Money

Withdraw money securely after account verification.

The system prevents:

* Invalid account access
* Negative withdrawals
* Withdrawals greater than the available balance

### 📋 Account Details

Users can securely view their:

* Name
* Age
* Email
* Account number
* Current balance

### ✏️ Update Account

Users can update:

* Name
* Email
* PIN

Their account number and balance remain unchanged.

### 🗑️ Delete Account

Accounts can be permanently deleted after authentication and confirmation.

### 📊 Dashboard

The Streamlit dashboard displays useful information such as:

* Total number of accounts
* Total money stored in the system
* System status

---

## 🛠️ Tech Stack

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| 🐍 Python    | Core programming & banking logic |
| 🧱 OOP       | Structuring the banking system   |
| 📄 JSON      | Local data persistence           |
| 🎨 Streamlit | Interactive web interface        |
| 🎲 Random    | Account number generation        |
| 📁 pathlib   | File handling                    |

---

## 🧠 How It Works

The application follows a simple architecture:

```text
             ┌─────────────────────┐
             │     Streamlit UI    │
             │                     │
             │  Create Account     │
             │  Deposit            │
             │  Withdraw           │
             │  View Details       │
             │  Update             │
             │  Delete             │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │      Bank Class     │
             │                     │
             │  Authentication     │
             │  Validation         │
             │  Transactions       │
             │  Account Management │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │      data.json      │
             │                     │
             │  Account Records    │
             │  Balance            │
             │  User Information   │
             └─────────────────────┘
```

The `Bank` class handles the actual banking operations, while Streamlit acts as the frontend.

---

## 📂 Project Structure

```text
Bank-Management-System/
│
├── app.py              # Streamlit application
├── data.json           # Local JSON database
├── main.py             # Optional CLI version
└── README.md           # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/subhajit404/Bank-Management-System.git
```

Move into the project directory:

```bash
cd Bank-Management-System
```

### 2️⃣ Install dependencies

```bash
python -m pip install streamlit
```

### 3️⃣ Create the database

Create a file named:

```text
data.json
```

and add:

```json
[]
```

### 4️⃣ Run the application

Instead of:

```bash
streamlit run app.py
```

you can use:

```bash
python -m streamlit run app.py
```

This is particularly useful on Windows if the `streamlit` command isn't available directly in your PATH.

---

## 🖥️ Application Flow

### Create Account

```text
Enter Personal Information
          ↓
Validate Age & PIN
          ↓
Generate Account Number
          ↓
Save Account
          ↓
Display Account Information
```

### Deposit

```text
Account Number + PIN
          ↓
Authenticate User
          ↓
Validate Amount
          ↓
Update Balance
          ↓
Save to JSON
```

### Withdraw

```text
Account Number + PIN
          ↓
Authenticate User
          ↓
Check Balance
          ↓
Withdraw Amount
          ↓
Save Updated Balance
```

---

## 🔐 Validation & Security

The project includes basic validation such as:

* Minimum account age of 18
* Exactly 4-digit PIN
* Maximum deposit of ₹10,000
* No negative transactions
* Insufficient-balance protection
* Account authentication using account number + PIN
* Confirmation before account deletion

> ⚠️ **Important:** This project is designed for learning and demonstration purposes. PINs are currently stored in plain text inside JSON. A production banking application should use secure password/PIN hashing, encryption, a proper database, audit logs, rate limiting, and stronger authentication.

---

## 📸 Screenshots

You can add screenshots of your Streamlit application here:

```text
screenshots/
│
├── dashboard.png
├── create-account.png
├── deposit.png
├── withdraw.png
└── account-details.png
```

Then include them in this README:

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

## 🔮 Future Improvements

This project can be taken much further.

### 🔐 Security

* [ ] Hash PINs
* [ ] Login/logout system
* [ ] OTP verification
* [ ] Session management
* [ ] Failed-login protection

### 💳 Banking Features

* [ ] Transaction history
* [ ] Money transfer between accounts
* [ ] Mini statement
* [ ] Interest calculation
* [ ] Account types
* [ ] Monthly statements
* [ ] Transaction IDs

### 🗄️ Database

Move from JSON to:

```text
SQLite
   ↓
PostgreSQL
   ↓
Production Database
```

### 📊 Analytics

Add charts for:

* Deposits
* Withdrawals
* Account growth
* Transaction volume
* Total deposits

### 🌐 Deployment

The application can eventually be deployed as a live web application so users can access it through a browser.

---

## 🎯 What I Learned

Building this project helped me practice:

* Python Object-Oriented Programming
* Classes and methods
* JSON file handling
* CRUD operations
* Data validation
* Exception handling
* Random account generation
* Streamlit application development
* Git & GitHub
* Structuring a real-world application

---

## 💡 Project Philosophy

> **Start simple. Understand the fundamentals. Then build bigger.**

This project started as a basic Python banking program and evolved into an interactive web application.

The goal wasn't to recreate an actual bank.

The goal was to understand how the pieces of a software system fit together.

---

## 👨‍💻 Author

**Subhajit Patra**

B.Tech Student | Python & Full-Stack Developer | Exploring AI/ML

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐.

It helps motivate further development!

---

### 📜 License

This project is created for **educational and learning purposes**.
