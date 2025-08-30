from db_connect import connect
import random

def create_account():
    account_name = input("Enter name = ")
    account_email = input("Enter email address = ")
    date_of_birth = input("Enter date of birth [YYYY-MM-DD] = ")
    address_present = input("Enter present address = ")
    amount = float(input("Enter opening balance = "))
    
    db = connect()
    cursor = db.cursor()
    account_id = 0
    
    while True:
        account_id = random.randint(10000000, 99999999)
        cursor.execute("SELECT account_id FROM bank_accounts WHERE account_id = %s", (account_id,))
        result = cursor.fetchone()
        
        if not result:
            break
            
    sql = "INSERT INTO bank_accounts (account_id, account_name, account_email, date_of_birth, address_present, amount) VALUES (%s, %s, %s, %s, %s, %s)"
    
    values = (account_id, account_name, account_email, date_of_birth, address_present, amount)
    
    cursor.execute(sql, values)
    db.commit()
    print(f"Account Created successfully with ID: {account_id}!")
    db.close()


def view_all_accounts():
    db=connect()
    cursor=db.cursor()
    cursor.execute("SELECT * FROM bank_accounts")
    bank_accounts=cursor.fetchall()
    print("<<--All Accounts-->>")
    for acc in bank_accounts:
        print(f"\nID: {acc[0]}\nName: {acc[1]}\nEmail: {acc[2]}\nDate of Birth: {acc[3]}\nPresent Address: {acc[4]}\nAmount: {acc[5]}\n..........")
    db.close()


def deposit_money():
    account_id=int(input("Enter Account Id: "))
    amount=float(input("Enter deposit amount: "))
    db=connect()
    cursor=db.cursor()
    cursor.execute("UPDATE bank_accounts SET amount = amount + %s WHERE account_id=%s", (amount,account_id))
    db.commit()
    print("Money Deposited successfully")
    db.close()


def withdraw_money():
    account_id=int(input("Enter Account Id: "))
    amount=float(input("Enter amount to withdraw: "))
    db=connect()
    cursor=db.cursor()
    cursor.execute("SELECT amount FROM bank_accounts WHERE account_id=%s", (account_id,))
    result=cursor.fetchone()
    if result and result[0]>=amount:
        cursor.execute("UPDATE bank_accounts SET amount = amount - %s WHERE account_id=%s", (amount,account_id))
        db.commit()
        print("Withdrawal successfully")
    else:
        print("Insufficient balance")

    db.close()        
   

def check_balance():
     account_id=int(input("Enter Account Id: "))
     db=connect()
     cursor=db.cursor()
     cursor.execute("SELECT account_name,amount FROM bank_accounts WHERE account_id=%s",(account_id,))
     result=cursor.fetchone()
     if result:
         print(f"Account Holder : {result[0]}, Blance : {result[1]}")
     else:
         print("Account not found")
     db.close()             




