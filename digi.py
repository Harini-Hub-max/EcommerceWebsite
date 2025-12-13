import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harini@2919",
    database="atm_db"
)
cursor = db.cursor()
def create_account():
    acc_no = int(input("Enter New Account Number: "))
    name = input("Enter Name: ")
    pin = int(input("Set 4-digit PIN: "))
    balance = float(input("Enter Initial Balance: "))

    try:
        cursor.execute(
            "INSERT INTO accounts (account_no, name, pin, balance) VALUES (%s, %s, %s, %s)",
            (acc_no, name, pin, balance)
        )
        db.commit()
        print("✅ Account Created Successfully")
    except:
        print("❌ Account Number Already Exists")


def check_balance(acc_no):
    cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc_no,))
    result = cursor.fetchone()
    print("Your Balance is:", result[0])

def withdraw(acc_no, amount):
    cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc_no,))
    balance = cursor.fetchone()[0]

    if amount <= balance:
        new_balance = balance - amount
        cursor.execute(
            "UPDATE accounts SET balance=%s WHERE account_no=%s",
            (new_balance, acc_no)
        )
        db.commit()
        print("Withdraw Successful")
        print("Remaining Balance:", new_balance)
    else:
        print("Insufficient Balance")

def deposit(acc_no, amount):
    cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc_no,))
    balance = cursor.fetchone()[0]

    new_balance = balance + amount
    cursor.execute(
        "UPDATE accounts SET balance=%s WHERE account_no=%s",
        (new_balance, acc_no)
    )
    db.commit()
    print("Deposit Successful")
    print("Updated Balance:", new_balance)

# Login
acc_no = int(input("Enter Account Number: "))
pin = int(input("Enter PIN: "))

cursor.execute(
    "SELECT * FROM accounts WHERE account_no=%s AND pin=%s",
    (acc_no, pin)
)

account = cursor.fetchone()

if account:
    while True:
        print("\n--- ATM MENU ---")
        print("1. Create New Account")
        print("2. Check Balance")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()

        elif choice == 2:
            check_balance(acc_no)

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            withdraw(acc_no, amount)

        elif choice == 4:
            amount = float(input("Enter amount to deposit: "))
            deposit(acc_no, amount)

        elif choice == 5:
            print("Thank you for using ATM")
            break

else:
        print("Invalid Choice")
