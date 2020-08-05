# def multiply(number):
#     """THIS FUNCTION MULTIPLIES NUMBERS BY 3"""
#     print("The answer is:", number * 3)
# multiply(2)

# name = 'slow'
# def print_name():
#     global name
#     name = "free"
#     print(name)
# print_name()

# import requests
# url_to_get = "http://checklight.pythonanywhere.com/streets"
# url_to_get = "http://jumia.com.ng"
# response_data = ""

# def make_request(url):
#     global response_data
#     response = requests.get(url)
#     response_data = response
# def check_for_success():
#     if response_data.status_code == 200:
#         print("Request was successful")

# def checking_url():
#     try:
#         response_data.json()
#         data = response_data.json()
#         keyz = data.keys()
#         print(keyz)
#     except:
#         response_data.content
#         print("data is content")

# make_request(url_to_get)
# check_for_success()
# checking_url()

# name1 = ['slow']
# name2 = reverse(name1)
# print(name1)
# print(name2)

def anagram(word, test_word):
    sorted_word = sorted(word.lower())
    sorted_test_word = sorted(test_word.lower())
    if sorted_test_word == sorted_word:
        print(test_word, word)
    else:
        print(test_word, "no work", word)

def palindrome(word):
    reversed_word = word[::-1]
    if reversed_word.lower() == word.lower():
        print(word, "work")
    elif reversed_word.lower() != word.lower():
        print(word, "no work")

anagram("elbow", "blow")
palindrome("dad")