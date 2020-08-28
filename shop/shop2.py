import connect as con
logged_in_user = False

while logged_in_user == False:

    task = input("\nWelcome to Tobi's shop\nPlease enter : 'admin' login as Admin\n'cus' login as Customer\n'end' to quit\n> ")

    if task == "admin":
        while True:
            work = input("Please enter :'su' to signup\n'si' to signin\n'add' to add products\n'quit' to quit\n> ")
            if work == "su":
            
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

            elif work == "si":
                
                # ############ Sign in ADMIN ###############

                input_username = input("Please enter your username : ")
                input_password = input("Please enter your password : ")

                data = con.fetch_admin_detail(input_username)
                if data:    
                    if data:
                        print("Username was correct ..!!")
                        if input_password == data[0]['password']:
                            print("Loggin Successfull..!!")
                            logged_in_user = input_username
                
                    else:
                        print("Sorry your password was wrong")

                else:
                    print("Username was wrong ..!!")

            elif work == "add":
                if logged_in_user:
                ############### ADD PRODUCTS ADMIN ###########
                    product = input("Please enter product name: ")
                    price = int(input("Please enter price : "))
                    qty = int(input("Please enter quantity: "))
                    con.add_products(product,price,qty)
                else:
                    print("Sorry you need to be logged in first.!!")
            elif work == "quit":
                break
    elif task == "cus":
        while True:
            new_work = input("Please enter : 'su' to signup\n'si' to signin\n'pur' to make purchase\n'quit' to quit\n'end' to end\n> ")
            if new_work == "su":

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
            elif new_work == "si":
    # ############ Sign in ###############

                input_username = input("Please enter your username : ")
                input_password = input("Please enter your password : ")

                data = con.customer_profile(input_username)
                if data:    
                    if data:
                        print("Username was correct ..!!")
                        if input_password == data[0]['password']:
                            print("Loggin Successfull..!!")
                            logged_in_user = input_username
                
                    else:
                        print("Sorry your password was wrong")

                else:
                    print("Username was wrong ..!!") ## ASSIGN THE USERNAME AS LOGGED IN USER GLOBALLY
                    break
    # #################PURCHASE#############
            elif new_work == "pur":

                if logged_in_user:
                    products_found = []
                    shopping_cart =[]

                    data = con.show_products()
                        
                    if logged_in_user == input_username:
                        for item in data:
                            product = item["product"]
                            price = item["price"]
                            qty = item["qty"]
                            products_found.append({"product":product,
                                                    "price":price,
                                                    "qty":qty})
                        print()                        
                        for index,item in enumerate(products_found):
                            print(index, item["product"],item["price"])
                        selected_option = int(input("Above are products in shop\nPlease pick one to make purchase\n> "))

                        print("\n###########################")
                        print(products_found[selected_option]["product"].upper())
                        print("###########################\n")
                        print("###########################\n")
                        print("price:",price,"quantity available:",qty)
                        print("###########################\n")
                        action = input("Please choose quantity to purchase: ")
                        for item in products_found:
                            products=products_found[selected_option]["product"]
                            price = products_found[selected_option]["price"]
                            qty = action
                            shopping_cart.append({"product":products,
                                                    "price":price,
                                                    "qty":qty})
                        print(shopping_cart)
                        # sale = int(price)*int(action)
                        # con.purchase(action)
                        # print("Your purchase:", sale)
                else:
                    print("Sorry you need to be logged in first.!!")
            elif new_work == "quit":
                if logged_in_user:
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
