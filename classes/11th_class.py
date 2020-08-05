# a=input("puh:")
# def sleep(*a): #variable positional argument
#     for i in a:
#         for x in i:
#             if x == x.lower():
#                 print(x.upper())
#             else:
#                 print(x.lower())

# sleep(a)

# def soon(**data): #variable keywords arguments
#     print(data)

# soon(ade=23,bolu=34,sola=24)
# def products(**data):#variable keywords arguments
#     for key in data:
#         print(key.upper(),":",data[key])
#     prices = sum(data.values())
#     print("Total:",prices)
        

# products(apple=300,beans=500,rice=400)

# def sort_value(*scattered_list, should_be_ascending = True):
#     scattered_list = list(scattered_list)
#     unique_words = ""
    # for i in range(len(scattered_list)):
    #     for i in range(len(scattered_list)-1):
    #         if scattered_list[i] > scattered_list[-1]:
    #             unique_words.append(scattered_list[i],scattered_list[i+1])
    # if should_be_ascending:
    #     print(unique_words)
    # else:
    #     print(unique_words[::-1])
#     for word in scattered_list:
#         if word not in unique_words:
#             unique_words.append(word)
#     if should_be_ascending:
#         print(unique_words)
#     else:
#         print(unique_words[::-1])
# sort_value("bleesings",should_be_ascending=True)

# def string_processor(string)

##FIBONACCI SEQUENCE WITH LOOP
# a = 5
# f = 0
# s = 1
# if a <=0:
#     print("The requested series is ", f)
# else:
#     print(f,s,end=" ")
#     for x in range(2,a):
#         next=f+s
#         print(next,end=" ")
#         f=s
#         s=next

##FIBONACCI SEQUENCE WITH RECURSION

# def fibRecursion(n):
#     if n<0:
#         print("please enter a positive integer!")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return (fibRecursion(n-1)+fibRecursion(n-2))


# def fib2(*n):
#     if (n <=0):
#         return n
#     else:
#         return(fib2(n-1)+fib2(n-2))

# for i in range(10):
#     print(fib2(i), end=" ")




# def recur_factorial(n):
#     if n == 0:
#         return n
#     else:
#         return n*recur_factorial(n-1)

# num = 5
# if num < 0:
#     print("ogbeni")
# elif num == 0:
#     print("Factorial of 0 is 1")
# else:
#     print("Factorial of",num,"is",recur_factorial(num))

# def tri_recursion(k):
#     if (k>0):
#         result = k+tri_recursion(k-3)
#         print(result)
#     else:
#         result= 0
    
#     return result

# print("\n\nRecursion")
# tri_recursion(9)

# lizz = input("> ")
# lizz = lizz.split(",")
# lizz = list(map(lambda string: int(string),lizz))

# def movable_numbers(lizz, differences = []):
#     if len(lizz) < 2:
#         return differences
#     else:
#         differences.append(lizz[1]-lizz[0])
#         return movable_numbers(lizz[1:],differences)
# print(movable_numbers(lizz)


class Calc:
    def add(self,*args):
        result = (sum(args))
        print(result)

s = Calc()
s.add(3,3,4,5)


