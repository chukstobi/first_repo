import random
import datetime
class Bankaccount:
    logged_user = False

    def register(self):
        name = input("Please enter your name - ")
        password = input("Please enter your password - ")
        account_number = random.randrange(0,10**10)

        file_name = "bank_app/bank_users_login.csv"
        file = open(file_name, "a")

        file.write(f"{name},{password},{account_number}\n")
        print("Successfully created account \n")
        print("Below are your details:\n",name,account_number)

    def login(self):

        name_input = input("Please enter your name - ")
        password_input = input("Please enter your password - ")

        file_name = "bank_app/bank_users_login.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(",")
            name = splitted_line[0]
            password = splitted_line[1]

            if name == name_input:
                print("Username was correct ..!!")
                if password_input == password:
                    print("Loggin Successfull..!!")
                    
                    self.logged_user = name_input
                    break
                else:
                    print("Sorry your password was wrong")

        else :
            print("Username was wrong ..!!")
    
    def __init__(self):
        self.balance = 0
        print("welcome to simple bank app")
    
    def deposit(self):
        if self.logged_user:
            amount = float(input("Enter amount to deposit: "))
            self.balance += amount
            today = datetime.datetime.now()
            date = f"{today.day}/{today.month}/{today.year}"
            file_name = "bank_app/transactions.csv"
            file = open(file_name, "a")

            file.writelines(f"{self.logged_user}:;{self.balance}:;{date}\n")
            file.close()
            print("\nAmount deposited: ",amount)
    
    def withdraw(self):
        if self.logged_user:
            file_name = "bank_app/transactions.csv"
            file = open(file_name, "r")
            data = file.read()

            for line in data.splitlines():
                splitted_line = line.split(":;")
                self.balance = float(splitted_line[1])
            amount = float(input("Enter amount to deposit: "))
            if self.balance >= amount:
                self.balance -= amount
                file_name = "bank_app/transactions.csv"
                file = open(file_name, "a")

                file.writelines(f"{self.logged_user}:;{self.balance}\n")
                file.close()
                print("\nYou withdrew:", amount,"\n","Your balance:",self.balance)
            else:
                print("Insufficient funds")
    
    def transfer(self,from_account,to_account,amount):
        # file_name = "bank_app/transactions.csv"
        # file = open(file_name, "a")

        # file.writelines(f"{self.logged_user}:;{self.balance}\n")
        # file.close()
        from_account.withdraw(amount)
        to_account.deposit(amount)
    
    def display(self):
        file_name = "bank_app/transactions.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(":;")
            self.balance = float(splitted_line[1])
        print("Net available balance =", self.balance)
    
    def begin(self):

            is_registered = input("Do you have an account (y/n): ")

            if is_registered == "y":

                self.login()

            elif is_registered == "n":

                self.register()
                print("Please Sign In  to continue..\n")
                self.login()

            choice = input("Please what would you like to do : ")

            if choice == "d":

                self.deposit()

            elif choice == "w":

                self.withdraw()
            
            elif choice == "t":
                from_account = self.logged_user
                to_account = input("Please enter beneficiary name: ")
                amount = int(input("Please enter beneficiary name: "))
                self.transfer(from_account,to_account,amount)
            elif choice == "b":
                self.display()


Bankaccount().begin()