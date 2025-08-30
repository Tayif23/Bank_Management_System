# Bank Management System 

This is a simple console-based Bank Management System built with Python, designed to perform basic banking operations. It connects to a **MySQL** database to store and manage all account information.

-----

### Features 

  * **Create Account:** Allows you to create a new bank account by providing personal details and an initial deposit.
  * **View All Accounts:** Displays a list of all existing bank accounts stored in the database.
  * **Deposit Money:** Enables you to add funds to a specific account by providing the account ID and amount.
  * **Withdraw Money:** Lets you withdraw money from an account, with a check for sufficient balance.
  * **Check Balance:** Quickly checks the current balance of a specific account using its ID.

-----

### Prerequisites 

Before running the project, make sure you have the following installed:

  * **Python:** The project is written in Python.
  * **MySQL Database:** You need a MySQL server to store the data.
  * **MySQL Connector for Python:** This library allows your Python script to connect to the MySQL database. You can install it using pip:
    ```bash
    pip install mysql-connector-python
    ```

-----

### Installation and Setup 

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Tayif23/Bank_Management_System.git
    ```

2.  **Navigate to the Project Directory:**

    ```bash
    cd Bank_Management_System
    ```

3.  **Database Setup:**

      * Create a new database in your MySQL server. For example: `CREATE DATABASE Bank_Management_System;`
      * Create a table named `bank_accounts` with the following schema:
        ```sql
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

4.  **Configure Database Connection:**

      * Open the `db_connect.py` file.
      * Update the connection details with your MySQL username, password, host, and database name.
        ```python
        def connect():
            return mysql.connector.connect(
                host="localhost",
                user="your_username",
                password="your_password",
                database="your_database_name"
            )
        ```

-----

### How to Run the Project 

1.  Open your terminal or command prompt.
2.  Navigate to the project's main folder.
3.  Run the main Python script:
    ```bash
    python main.py
    ```
4.  Follow the on-screen instructions to perform banking operations.

