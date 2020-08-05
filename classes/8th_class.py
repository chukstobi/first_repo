# import random

# name = input("puh name: ")
# maiden_name = input("maiden name: ")
# password_length = int(input("length: "))

# full_word = name + maiden_name
# password = "a"
# for letter in range(password_length):
#     while True:
#         random_choice = random.randint(0, len(full_word)-1)
#         if full_word[random_choice] not in password:                   
#             break

#     password = password + full_word[random_choice]
# print(password)

# scattered_list = [1,3,4,7,2,5,6]
# disorder_found = True
# for i in range(len(scattered_list)):
#     for i in range(len(scattered_list)-1):
#         if scattered_list[i] > scattered_list[i+1]:
#             scattered_list[i], scattered_list[i+1] = scattered_list[i+1], scattered_list[i]
#             print(scattered_list)
# dictionary = {}
# while True:
#     key = input('Please enter key: ')
#     value = input('kindly enter value: ')
#     dictionary[key] = value

#     print(dictionary)
    
numbers = [3,4,5,6,3,5,7,98,4]

unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
        print(unique)