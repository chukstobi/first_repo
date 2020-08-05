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
                file = open("shop/admin_db.csv", "a")
                file.write(f"{firstname},{surname},{username},{password}\n")
                file.close()
            
            elif work == "si":
                
                # ############ Sign in ADMIN ###############

                input_username = input("Please enter your username : ")
                input_password = input("Please enter your password : ")

                file = open("shop/admin_db.csv", "r")

                for line in file.readlines():
                    saved_username, saved_password = line.replace("\n","").split(",")[2:]
                    
                    if saved_username.lower() == input_username.lower():
                        if input_password == saved_password:
                            print(f"Welcome {saved_username}")
                            logged_in_user = saved_username ## ASSIGN THE USERNAME AS LOGGED IN USER GLOBALLY
                            break
                else:
                    print("Sorry you may not have an account, Please sign up.")

            elif work == "add":
                if logged_in_user:
                ############### ADD PRODUCTS ADMIN ###########
                    product = input("Please enter product name: ")
                    price = int(input("Please enter price : "))
                    qty = int(input("Please enter quantity: "))
                    file = open("shop/products.csv", "a")

                    file.write(f"{product},{price},{qty}\n")
                    file.close()
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
                file = open("shop/customer_db.csv", "a")
                file.write(f"{firstname},{surname},{username},{password}\n")
                file.close()
            elif new_work == "si":
    # ############ Sign in ###############

                input_username = input("Please enter your username : ")
                input_password = input("Please enter your password : ")

                file = open("shop/customer_db.csv", "r")

                for line in file.readlines():
                    saved_username, saved_password = line.replace("\n","").split(",")[2:]
                    
                    if saved_username.lower() == input_username.lower():
                        if input_password == saved_password:
                            print(f"Welcome {saved_username}")
                            logged_in_user = saved_username ## ASSIGN THE USERNAME AS LOGGED IN USER GLOBALLY
                            break
    # #################PURCHASE#############
            elif new_work == "pur":

                if logged_in_user:
                    products_found = []

                    file = open("shop/products.csv", "r")
                    for product in file.readlines():
                        product, price, qty = product.split(",")
                        
                        if logged_in_user == input_username:
                            products_found.append({
                                                    "product":product,
                                                    "price":price,
                                                    "qty":qty
                                                })
                    print()
                    for index, product in enumerate(products_found):
                        print(index+1, product["product"])
                    print()
                    selected_option = int(input("Above are products in shop\nPlease pick one to make purchase\n> "))

                    print("\n###########################")
                    print(products_found[selected_option-1]["product"].upper())
                    print("###########################\n")
                    print("price:",products_found[selected_option-1]["price"],"quantity available:", products_found[selected_option-1]["qty"])
                    print("###########################\n")
                    action = input("Please choose quantity to purchase: ")
                    sale = int(products_found[selected_option-1]['price'])*int(action)
                    print("Your purchase:", sale)
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
