# import time
# import winsound
# for i in range(60):
#     print()
#     # aim = int(input("please input time in mminute: "))
#     time.sleep(1)
#     winsound.Beep(1000, 20)
# winsound.Beep(1000, 400)

# import time

# minutes = 3
# seconds = minutes * 60

# for i in reversed(range(seconds)):
#     print(int(i/60), i%60, sep = ":")
#     time.sleep(1)

# import winsound

# value = 10
# for  i in reversed(range(value)):
    
#     print(i)
#     for i in range(5):
#         winsound.Beep(1000, 20)
# winsound.Beep(1000, 400)



# for i in reversed(range(minutes)):
#     for j in reversed(range(60)):
#         print(i, j, sep = ":")
#         time.sleep(1)

# import time
# while True:
#     try:
#         minutes = int(input("Please enter minute: "))
#         seconds = minutes * 60
#         for i in reversed(range(seconds)):
#             mins, secs = divmod(i, 60)
#             print(mins, secs, sep = ":")
#             time.sleep(1)
#     except:
#         print("Please enter minute in number.")
#     continue

# TO APPEND
names = ['lola', 'seun']
print(names)
# for i in range(10):
#     names.append("shina")
# for j in range(5):
#     names.append("salam")
# print("After appending")
# print(names)
print("After Remove:")
names.remove('seun')
print(names)
