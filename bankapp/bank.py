import random
import connect as con 

class Bank():

    logged_user = False
    balance = 0

    def get_new_acct_no(self):

        new_acct = random.choice(range(1,9999999))
        max_chars = 8
        current_acct_chars = len(str(new_acct))

        deficiency = max_chars - current_acct_chars

        if  deficiency:
            new_acct = ("0"*deficiency) + str(new_acct)
        
        return new_acct

    def register(self):
        
        name = input("Please enter your name - ")
        age = int(input("Please enter your age - "))
        password = input("Please enter your password - ")

        # con.create_table()
        con.ad_users(name,age,password,self.get_new_acct_no())
        print("Successfully created account \n")

    def login(self):

        name_input = input("Please enter your name - ")
        password_input = input("Please enter your password - ")
        
        data = con.fetch_user_detail(name_input)
        if data:
            print("Username was correct ..!!")
            if password_input == data[0]['password']:
                print("Loggin Successfull..!!")
                
                self.logged_user = name_input
                self.balance = data[0]['balance']
                
            else:
                print("Sorry your password was wrong")

        else:
            print("Username was wrong ..!!")

    def read_data(self):
        data = con.fetch_detail()
        
        for index,line in enumerate(data):
            print(index,line['name'])


    def read_user_data(self):
        data = con.show_user_detail(self.logged_user)
        print(data)
        
    def get_balance(self):
        data = con.get_balance(self.logged_user)
        balance = data[0]['balance']
        print(f"Name:{self.logged_user}\nBalance:{balance}")

    def deposit(self, amount, name = "self"):

        target_name = name if name != "self" else self.logged_user
        
        original_balance = con.get_balance(target_name)[0]['balance']
        bal = int(original_balance) + amount
        con.alter_balance(target_name,bal)
        con.log(name=self.logged_user,destination=self.logged_user,type='deposit',amount=amount)
        print("Deposit Successfull...!")
    
    def withdraw(self, amount):
        original_balance = con.get_balance(self.logged_user)[0]['balance']
        bal = int(original_balance) - amount
        con.alter_balance(self.logged_user,bal)
        con.log(name=self.logged_user,destination=self.logged_user,type='withdrawal',amount=amount)
        print("Withdrawal Successfull...!")

    def transfer(self, amount, target):

        self.withdraw(amount)

        self.deposit(amount, target)
        con.log(name =self.logged_user,destination=target,type = 'transfer',amount=amount)
    def show_user_account_statement(self):
        data=con.show_user_statement(self.logged_user)
        filename = "user_statement.csv"
        file_work=open(filename,'w')
        file_work.write(f"name,type,destination,amount,\n")

        for item in data:
            name=item['name']
            type=item['type']
            destination=item['destination']
            amount=item['amount']
            file_work.write(f"{name},{type},{destination},{amount}\n")
    
    def begin(self):
        self.logged_user=False
        while self.logged_user == False:
            task = input("Welcome to KBank.....\nTo Sign up press 'su'\nTo Login press 'Lo'!\n> ")
            if task == "su":
                self.register()
            elif task == "lo":
                self.login()
            elif task == "q":
                pass
            if self.logged_user:
                new_task = input("What would you like to do?\n'D' for Deposit\n'W' for withdraw\n'T' for Transfer\n'B' for balance\n'UD' for Biodata\n'Q' for quit.!\n> ")
                if new_task == "d":
                    amount = int(input("please amount to deposit: "))
                    self.deposit(amount)
                elif new_task == "w":
                    amount = int(input("please amount to withdraw: "))
                    self.withdraw(amount)
                elif new_task == "t":
                    amount = int(input("please amount to transfer: "))
                    receiver = input("please name of recipient: ")
                    self.transfer(amount,receiver)
                elif new_task == "b":
                    self.get_balance()
                elif new_task == "ud":
                    self.read_user_data()
                elif new_task == "s":
                    self.show_user_account_statement()
                elif new_task == "q":
                    print("look")
                    new_task
        # elif new_task == "q":
        #         confirmation = input("Are you sure you want to quit? Y/N: ")
        #         if confirmation == "Y":
        #             print("Thanks for your patronage.")
        #             break
        #         else:
        #             new_task

bank = Bank()
bank.begin()