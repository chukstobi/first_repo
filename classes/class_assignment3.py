# import random
# players = [["unnamed", 0],["unnamed", 0], ["unnamed", 0], ["unnamed", 0]]
# for index in range(len(players)):
#     players[index][0] = input(f"Please enter name for player {index}: ")
# for index, player in enumerate(players):
#     name = player[0]
#     score = player [1]
#     lucky_number = input(f"Hello {name} please press your lucky number and enter to roll: ")
#     for number in lucky_number:
#         # for rolled_number in number:
#         rolled_number = random.randint(1,6)
#     players[index][1] += rolled_number
#     score += rolled_number
#     # if players > 20:
#     #     winning_player = players[index] + score > 20
#     #     print(f"welldone {winning_player} won")
#     #     break
#     print(name, "\n", score, end = "\n\n")
# print(players)

names = ['sade']
sub_names = ['bolu']
for char in names:
    for j in sub_names:
        print(char)