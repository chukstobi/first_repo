### ALGORITHMS ######

### STRING MANIPULATION
## REVERSE INTEGER

# def solution(x):
#     string = str(x)

#     if string[0] == '-':
#         return int('-'+string[:0:-1])
#     else:
#         return int(string[::-1])

# print(solution(-231))
# print(solution(345))

##AVERAGE WORD LENGTH
def solution(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p,'')
    words = sentence.split()
    return round(sum(len(word) for word in words )/len(words),2)

sentence = "Hi all, my nameis Tom... I am originally from Australia."
print(solution(sentence))