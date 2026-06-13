class ATM:
    def __init__(self):
        self.balance = 10000
        self.pin = "1234"
 
    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
 
        if entered_pin == self.pin:
            print("Login Successful!")
            self.menu()
        else:
            print("Invalid PIN!")
 
    def menu(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
 
            choice = input("Enter your choice: ")
 
            if choice == "1":
                self.check_balance()
 
            elif choice == "2":
                self.deposit()
 
            elif choice == "3":
                self.withdraw()
 
            elif choice == "4":
                print("Thank you for using ATM!")
                break
 
            else:
                print("Invalid Choice!")
 
    def check_balance(self):
        print("Available Balance:", self.balance)
 
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("Amount Deposited Successfully!")
        print("Updated Balance:", self.balance)
 
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
 
        if amount <= self.balance:
            self.balance -= amount
            print("Please collect your cash.")
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance!")
 
atm = ATM()
atm.verify_pin()
 