def create_account():
    account_name = input("Full Name: ")
    date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
    age = int(input("Age: "))
    address_present = input("Present Address: ")
    address_permanent = input("Permanent Address: ")
    amount = float(input("Initial Deposit (BDT): "))
    account_id = "AC" + ''.join(random.choices(string.digits, k=6))
    created_on = datetime.now().strftime("%Y-%m-%d")

    db=connect()
    cursor=db.cursor()
    sql="INSERT INTO accounts (account_id, account_name, date_of_birth, age, address_present, address_permanent, amount, created_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(%account_id, account_name, date_of_birth, age, address_present, address_permanent, amount, created_on)

    cursor.execute(sql,values)
    db.commit()
    print("Account created! ID: {account_id}")
    db.close()


def create_account():
    name=input("Enter your First name = ")
    balance=float(input("Enter your opening balance = "))
    db=connect()
    cursor=db.cursor()
    sql="INSERT INTO accounts (name,balance) VALUES (%s,%s)"
    values=(name,email,balance)
    cursor.execute(sql,values)
    db.commit()
    print("Account Created successfully!")
    db.close()