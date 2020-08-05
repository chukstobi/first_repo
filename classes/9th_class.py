###################COMPLICATED NOTEPAD#################

# ########SIGN UP########

# firstname = input("Please enter name: ")
# surname = input("Please enter surname: ")
# username = input("Please enter username: ")
# password = input("Please enter password: ")
# confirm_password = input("Please confirm password: ")

# file = open("notepad/db.csv", "a")
# file.write(f"{firstname},{surname},{username},{password}\n")
# file.close

# ########SIGN IN########
# input_username = input("Please enter username: ")
# input_password = input("Please enter password: ")
# file = open("notepad/db.csv", "r")
# for line in file.readlines():
#     saved_username, saved_password = line.split(",")[2:]
#     if saved_username.lower() == input_username.lower() and saved_password.replace("\n","") == input_password:
#         print(f"Welcome {saved_username}")
#         break
# else:
#     print(saved_username,saved_password,"sorry, username/or password not correct\nPlease check for errors or sign up!.")

# ########WRITE JOURNAL########

# import datetime

# title = input("Please enter title: ")
# note = input("Please enter note: ")
# today = datetime.datetime.now()
# date = f"{today.day}/{today.month}/{today.year}"
# username = "bola_ige"

# file = open("notepad/journals.csv", "a")
# file.write(f"{username},{title},{note},{date}\n")
# file.close()

# ########READ JOURNAL########

logged_in_username = "bola_ige"
journals_found = []

file = open("notepad/journals.csv", "r")
for line in file.readlines():
    username, title, body, date = line.split(",")
    if logged_in_username == username:
        journals_found.append({
            "title":title,
            "note":note
        })
print()
for index, journal in enumerate(journals_found):
    print(index+1, journal["title"])
print()
selected_option = int(input("Above are your notes pick one\n> "))
print("\n#######################")
print(journals_found[selected_option-1]["title"].upper())
print("#######################\n")
print(journals_found[selected_option-1]["note"])
print("\n#######################")
print("#######################\n")

# ########DELETE JOURNAL########
logged_in_username = "bola_ige"
journals_found = []

file = open("notepad/journals.csv", "r")
for line in file.readlines():
    username, title, note, date = line.split(",")
    if logged_in_username == username:
        journals_found.append({
            "title":title
            "note":note
        })
file.close()
print()

for index, journal in enumerate(journals_found):
    print(index+1, journal["title"])
print()
selected_option = int(input("Select a journal to delete\n> "))



