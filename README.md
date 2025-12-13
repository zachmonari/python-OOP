# 🧾 Mini Payment System with Admin Dashboard

A fully functional **Python + Streamlit** mini payment system featuring mobile-money simulation, multi-currency support, PDF receipts, database storage, admin dashboard, export tools, and dark mode.

---

## 🚀 Features

### 🔹 User Features

* Mobile money simulation (fake OTP + delay)
* Multiple payment methods (M-Pesa, Card, PayPal, etc.)
* Automatic currency conversion (API-based or local rates)
* Auto-generated **PDF receipts**
* Clean Streamlit UI
* Dark / Light mode toggle

### 🔹 Admin Dashboard

* User role login (**Admin / Viewer**)
* Full transaction table
* Filters:

  * Date range
  * Payment method
  * Currency
  * Status (if enabled)
  * Search bar
* Live charts:

  * Daily revenue trend
  * Payments by method
  * Currency breakdown
* Export filtered data as **CSV**
* View / download PDF receipts
* Refresh data
* (Admin only) Danger zone controls

---

## 📁 Project Structure

```
project/
│── app.py                     # Main user payment UI
│── pages/
│     └── 1_Admin_Dashboard.py # Full admin dashboard
│── admin/
│     └── queries.py           # fetch_transactions() and DB calls
│── models.py                  # SQLAlchemy models
│── database.py                # SessionLocal and engine
│── receipts/                  # Auto‑generated PDF receipts
│── README.md                  # This file
```

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** (Frontend UI)
* **SQLite / PostgreSQL** (Storage)
* **SQLAlchemy** (ORM)
* **ReportLab** (PDF builder)
* **Requests** (Currency conversion API)

---

## ▶️ How to Run the App

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Initialize the database

```bash
python database.py
```

### 3️⃣ Start the Streamlit app

```bash
streamlit run app.py
```

### 4️⃣ Open the Admin Dashboard

Streamlit automatically detects pages:

```
http://localhost:8501/1_Admin_Dashboard
```

---

## 🔐 Default Credentials

You can change these in `1_Admin_Dashboard.py`:

```
admin  / admin123   (Admin)
viewer / viewer123  (Read-only)
```

---

## 📦 Exporting Data

The admin dashboard allows:

* Download CSV of filtered transactions
* Download individual PDF receipts

---

## 📊 Visualizations

* Revenue per day (line chart)
* Amount collected by payment method (bar)
* Currency totals (table)

---

## 🧩 Future Enhancements

* Emailing receipts automatically
* Real API currency rates (Fixer, ExchangeRate API)
* JWT-based authentication
* Dashboard analytics using Plotly
* Admin CRUD for users

---

## ❤️ Created By

**Zachary Monari** — Mechanical engineering student & software creator building modern, clean, data-driven apps with Streamlit.

---


