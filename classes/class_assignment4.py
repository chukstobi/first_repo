names = "john"
names_rep = "sade"
names_rep2 = "slik"

for j in names:
    for i in names_rep:
        for c in names_rep2:
            print(j, i, c)

# read_or_write = input("What would you like to do \n R for read W for write: ")
# if read_or_write.lower() == "w":
#     name = input("Please enter your Username: ")
#     password = input("Please enter your password: ")

#     user_detail_file = open("data/{}_detail.csv".format(name), "w")
#     user_detail_file.write(f"{name},{password}")

#     database = open(f"data/{name}_database.txt", "a")

#     data = input("please enter your note: ")
#     database.write(f"{data}\n")
# elif read_or_write.lower() == "r":
#     name = input("Please enter your unsername: ")
#     password_input = input("Please enter your password: ")

#     user_detail_file = open("data/{}_detail.csv".format(name), "r")
#     username, password = user_detail_file.readline().split(",")

#     username_is_correct = username == name
#     password_is_correct = password == password_input

#     if username_is_correct and password_is_correct:
#         database = open(f"data/{name}_database.txt", "r")
#         data = database.read()
#         print(data)
# user_detail_file.close()