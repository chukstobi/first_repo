# file = open("timestable.csv", "w")
# number1 = range(5)
# number2 = range(5)

# for i in number1:
#     text = ""
#     for j in number2:
#         # print(f"{i}X{j} = {i*j}".center(10), end="")
#         print(i, "*", j, "=", i*j, sep =",", end = '\t')
#         text += i, "*", j, "=", i*j

#     print(text, file = file, end="\n")
#     print()
        
# for i in range(1,5):
#     text = ""
#     for j in range(1,5):
#         print(f"{i}X{j} = {i*j}".ljust(10), end = "")
#         text += f"{i}X{j} = {i*j},".ljust(10)
#     print(text, file = file, end="\n")
#     print()

# total_even = 0
# total_odd = 0
# highest_even_ratio = 0

# for i in range(1, 101):
#     if i%2 == 0:
#         total_even += i
#     else:
#         total_odd += i
#     if i%10 == 0:
#         ratio = total_even/total_odd
#         if ratio > highest_even_ratio:
#             highest_even_ratio = ratio
#         print("Decade -", i, "Even -", total_even, "Odd -", total_odd, "Ratio -", ratio)
#         total_even = 0
#         total_odd = 0
# print("Highest even ratio: ", highest_even_ratio)
    