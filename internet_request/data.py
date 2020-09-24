# first_file ="LSETF August 2020 - Revoked.csv"
# file = open(first_file,'r')
# revoked_list = file.read()



# second_list = open("qualified_list.csv","r")
# qualified_list = second_list.read()

# blow = []
# win = []

# for item in revoked_list.splitlines():
#     data = item.split(',')
#     # Name = data[1]
#     Email = data[2]
#     blow.append({"Email":Email})

# for item in qualified_list.splitlines():
#     work = item.split(',')
#     email = work[1]
#     First_name = work[2]
#     Last_name = work[3]
#     Phone = work[4]
#     win.append({"First_name":First_name,
#                 "Last_name":Last_name,
#                 "Phone":Phone,
#                 "email":email})

# print(blow[0])
# for name in win:
#     for w in name["email"]:
#         for s in blow:
#             if w == s:
#                 print(win)
#                 continue


# # crow = ben.pop(0)
# # for shark in ben:
# #     wine = shark.split(",")
# #     if wine[1] != str:
# #         print(type(wine[1]))
# #         print(type(wine[1]))


# # for email in range(0,len(qualified_list.splitlines())):
# #     print(email)
#     # craze = email.split(",")
#     # name = craze[0]
#     # chu = craze[8]
#     # ben += 1
#     # print(name,chu)

file1_name = "LSETF August 2020 - Revoked.csv"
file1 = open(file1_name,"r").readlines()

file2_name= "qualified_list.csv"
file2 = open(file2_name,"r").readlines()

lame = []
dame = []
for d in file1:
    same = d.split(",")
    dame.append(same[1])
for s in file2:
    sim = s.split(",")
    see = sim[1]
    for shame in dame:
        while see == shame:
            print(shame)