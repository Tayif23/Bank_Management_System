#  Bank Management System

This is a **GUI-based Bank Management System** built with **Python's CustomTkinter** library.  
The application provides a modern and user-friendly interface for common banking operations such as **account creation, fund management, and balance inquiry**.

---

##  Features

- **Create Account**  – Allows new users to create an account by providing personal details and an initial deposit.  
- **View All Accounts**  – Displays a list of all existing bank accounts in a scrollable table format.  
- **Deposit Money**  – Enables users to add funds to a specific account using its ID.  
- **Withdraw Money**  – Allows users to withdraw money, with checks for sufficient balance.  
- **Check Balance**  – Provides a quick way to view the current balance of an account by entering the account ID.  
- **Modern GUI**  – Two-panel layout with responsive images, consistent typography, and dynamic button styling.  

---

##  Technologies Used

- **Python** – Core programming language  
- **CustomTkinter** – Modern and responsive GUI library for Python  
- **Pillow (PIL)** – Image handling and resizing  
- **Threading** – Keeps the GUI responsive during operations  
- **MySQL** – Relational database for persistent storage  

---

##  Database Setup

This project uses **MySQL** to store account information.  
Before running the application, create the database and table using the following SQL commands:

```sql
CREATE DATABASE Bank_Management_System;
USE Bank_Management_System;

CREATE TABLE bank_accounts (
    account_id VARCHAR(20) PRIMARY KEY,
    account_name VARCHAR(100),
    account_email VARCHAR(100),
    date_of_birth DATE,
    address_present VARCHAR(255),
    amount NUMERIC(12, 2)
);
```
## How to Run the Project

1. Clone the repository or download the project files.

2. Make sure Python and MySQL are installed on your system.

3. Set up the database as shown above.

4. Install the required Python libraries:
```
pip install customtkinter Pillow mysql-connector-python

```
5. Run the main application file:
```
python gui_app.py
```

The application will launch, and you can begin performing bank management tasks.

