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
        