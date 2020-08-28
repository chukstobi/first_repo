import connect as con
class Shop:
    logged_in_user = False
    def admin_signup(self):
        # ############# Sign UP for ADMIN ##############

        print("Welcome to Tobi's store\nWe are offering 10% Discount on sales above N50,000")
        firstname = input("Please enter your First name : ")
        surname = input("Please enter your surname : ")
        username = input("Please enter your username : ")

        password = input("Please enter your password : ")
        confirm_password = input("Please re-enter your password : ")

        while password != confirm_password:

            print("Sorry you passwords dont match !!\n")
            password = input("Please enter your password : ")
            confirm_password = input("Please re-enter your password : ")
        con.add_admins(firstname,surname,username,password)
                
    def admin_login(self):
        # ############ Sign in ADMIN ###############

        input_username = input("Please enter your username : ")
        input_password = input("Please enter your password : ")

        data = con.fetch_admin_detail(input_username)
        if data:    
            if data:
                print("Username was correct ..!!")
                if input_password == data[0]['password']:
                    print(data[0]['password'])
                    print("Loggin Successfull..!!")
                    self.logged_in_user = input_username
        
            else:
                print("Sorry your password was wrong")

        else:
            print("Username was wrong ..!!")

    def admin_add_products(self):
        if self.logged_in_user:
            product = input("Please enter product name: ")
            database_price_product = con.show_products(product)
            if database_price_product:                
                if product == database_price_product[0]['product']:
                    old_qty = database_price_product[0]['qty']
                    price = int(input("Please enter price : "))
                    qty = int(input("Please enter quantity: "))
                    new_qty = old_qty + qty
                    data = con.fetch_admin_detail(self.logged_in_user)
                    adminsID = data[0]["adminsID"]
                    con.update_productname_price_qty(product,price,new_qty,adminsID)
            else:
                price = int(input("Please enter price : "))
                qty = int(input("Please enter quantity: "))
                data = con.fetch_admin_detail(self.logged_in_user)
                adminsID = data[0]["adminsID"]
                con.add_products(product,price,qty,adminsID)
        else:
            print("Sorry you need to be logged in first.!!")

    def customer_signup(self):
    # ############# Sign UP for customers ##############

        print("Welcome to Tobi's store\nWe are offering 10% Discount on sales above N50,000")
        firstname = input("Please enter your First name : ")
        surname = input("Please enter your surname : ")
        username = input("Please enter your username : ")

        password = input("Please enter your password : ")
        confirm_password = input("Please re-enter your password : ")

        while password != confirm_password:

            print("Sorry you passwords dont match !!\n")
            password = input("Please enter your password : ")
            confirm_password = input("Please re-enter your password : ")
        con.add_customers(firstname,surname,username,password)
                
    def customer_login(self):
        # ############ Sign in ###############

        input_username = input("Please enter your username : ")
        input_password = input("Please enter your password : ")

        data = con.customer_profile(input_username)
        if data:    
            if data:
                print("Username was correct ..!!")
                if input_password == data[0]['password']:
                    print("Loggin Successfull..!!")
                    self.logged_in_user = input_username
        
            else:
                print("Sorry your password was wrong")

        else:
            print("Username was wrong ..!!") 
            # break
        # #################PURCHASE#############
                
    def purchase_product(self,input_username):
        if self.logged_in_user:
            
            products_found = []
            shopping_cart =[]

            data = con.show_all_products()
            customer_profile = con.customer_profile(self.logged_in_user)
            customerID = customer_profile[0]['customerID']
                
            if self.logged_in_user == input_username:
                for item in data:
                    product = item["product"]
                    price = item["price"]
                    qty = item["qty"]
                    products_found.append({"product":product,
                                            "price":price,
                                            "qty":qty})
                print()                        
                for index,item in enumerate(products_found):
                    print(index, item["product"],item["price"],item["qty"])
                selected_option = int(input("Above are products in shop\nPlease pick one to make purchase\n> "))

                print("\n###########################")
                print(products_found[selected_option]["product"].upper())
                print("###########################\n")
                print("price:",products_found[selected_option]["price"],"quantity available:",products_found[selected_option]["qty"])
                print("###########################\n")
                qty = int(input("Please choose quantity to purchase: "))
                products=products_found[selected_option]["product"]
                price = products_found[selected_option]["price"]
                sales = int(price)*qty
                full_qty = products_found[selected_option]["qty"] - qty
                shopping_cart.append({"product":products,
                                        "price":price,
                                        "qty":qty,
                                        "full_qty":full_qty,
                                        "sales":sales})
                more_purchase = input("would you like to make more purchase Y/N: ")
                while more_purchase == "y":
                    for index,item in enumerate(products_found):
                        print(index, item["product"],item["price"],item["qty"])
                    selected_option = int(input("Above are products in shop\nPlease pick one to make purchase\n> "))
                    print("\n###########################")
                    print(products_found[selected_option]["product"].upper())
                    print("###########################\n")
                    print("###########################\n")
                    print("price:",products_found[selected_option]["price"],"quantity available:",products_found[selected_option]["qty"])
                    print("###########################\n")
                    qty = int(input("Please choose quantity to purchase: "))
                    products = products_found[selected_option]["product"]
                    price = products_found[selected_option]["price"]
                    sales = int(price)* qty
                    full_qty = products_found[selected_option]["qty"] - qty
                    shopping_cart.append({"product":products,
                                            "price":price,
                                            "qty":qty,
                                            "full_qty":full_qty,
                                            "sales":sales})
                    more_purchase = input("would you like to make more purchase Y/N: ")
                    
                
                print("\nYour selected products,prices and quantities\n")
                total_price = []
                total_qty = []
                total_sales = []
                for index,item in enumerate(shopping_cart):
                    total_price.append(int(item['price']))
                    total_qty.append(int(item['qty']))
                    total_sales.append(int(item['sales']))
                    print(f"{index} - product:{item['product']} price:{item['price']} Qty:{item['qty']}")

                new_total_sales = 0
                if total_sales:
                    new_total_sales = sum(total_sales)
                print("Your purchase:",new_total_sales,"\nThanks for your patronage!")
                for qty in shopping_cart:
                    total_qty = qty['full_qty']
                    total_product = qty['product']
                    each_qty = qty['qty']
                    each_price = qty['price']
                    
                    con.purchase(total_qty,total_product)
                    con.log(customerID,each_price,each_qty,total_product)
        else:
            print("Sorry you need to be logged in first.!!")

    def begin(self):
        while self.logged_in_user == False:
            task = input("\nWelcome to Tobi's shop\nPlease enter : 'admin' login as Admin\n'cus' login as Customer\n'end' to quit\n> ")

            if task == "admin":
                while True:
                    work = input("Please enter :'su' to signup\n'si' to signin\n'add' to add products\n'quit' to quit\n> ")
                    if work == "su":
                        self.admin_signup()
                    elif work == "si":
                        self.admin_login()
                    elif work == "add":
                        self.admin_add_products()
                    elif work == "quit":
                        break
            elif task == "cus":
                while True:
                    new_work = input("Please enter : 'su' to signup\n'si' to signin\n'pur' to make purchase\n'quit' to quit\n'end' to end\n> ")
                    if new_work == "su":
                        self.customer_signup()
                    elif new_work == "si":
                        self.customer_login()
                    elif new_work == "pur":
                        self.purchase_product(self.logged_in_user)
                    elif new_work == "quit":
                        if self.logged_in_user:
                            confirmation = input("Are you sure you want to quit? Y/N: ")
                            if confirmation == "Y":
                                print("Thanks for your patronage.")
                                break
                            else:
                                new_work
                        else:
                            print("Sorry you need to be logged in first.!!")
                    elif new_work == "end":
                        break
            elif task == "end":
                break

shop = Shop()
shop.begin()