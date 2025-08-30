import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12Tay*66F",
        database="Bank_Management_System"
    )
