# file = open("application_data.csv", "r")
# write_file = open("application_data_copy.csv", "w")

# for line_number, line in enumerate(file.readlines()):
#     if line_number == 0:
#         line_to_write = line.replace("\n", "") + "," + "payback" + "," + "InterestValue" + "\n"
#         # print(line_to_write)
#         write_file.write(line_to_write)
#         continue
#     values = line.split(",")
#     amount, interest = float(values[4]), float(values[5])

#     payback = amount + (amount * (interest/100))
#     interest_value = amount * (interest/100)

#     line_to_write = line.replace("\n", "") + "," + str(payback) + "," + str(interest_value) + "\n"
#     # print(line_to_write)
#     write_file.write(line_to_write)

for i in range(100, 999):
    sum_nums = i + i + i
    last_char_of_num = str(i)[2]*3
    sum_nums_as_str = str(sum_nums)
    print(i, sum_nums, last_char_of_num, sum_nums_as_str == last_char_of_num)
    if sum_nums_as_str == last_char_of_num: break;

