Bank Management System
This is a GUI-based Bank Management System built with Python's CustomTkinter library. The application provides a simple and user-friendly interface for common banking operations, including account creation, fund management, and balance inquiry.

Features
Create Account: Allows new users to create an account by providing personal details and an initial deposit.

View All Accounts: Displays a list of all existing bank accounts in a scrollable table format.

Deposit Money: Enables users to add funds to a specific account using its ID.

Withdraw Money: Allows users to withdraw money from an account, with checks for sufficient balance.

Check Balance: Provides a quick way to view the current balance of an account by entering the account ID.

Modern GUI: The user interface is designed with a two-panel layout, featuring responsive images, consistent typography, and dynamic button styling.

Technologies Used
Python: The core programming language.

CustomTkinter: A modern and responsive GUI library for Python.

Pillow (PIL): Used for handling and resizing images within the application.

Threading: Implemented to perform bank operations in a separate thread, ensuring the GUI remains responsive.

MySQL: The relational database used for persistent storage of all bank account data.

Database Setup
This project uses a MySQL database to store account information. Before running the application, you need to set up the database and the required table. Use the following SQL commands to create the Bank_Management_System database and the bank_accounts table.

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

How to Run the Project
Clone this repository or download the project files.

Ensure you have Python and MySQL installed.

Set up the database as described in the "Database Setup" section above.

Install the required Python libraries using pip:

pip install customtkinter Pillow mysql-connector-python

Run the main application file:

python gui_app.py

The application will launch, and you can begin performing bank management tasks.
