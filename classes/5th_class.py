# s = 0
# while s < 10:
#     s += 1
#     print(s)

# import random
# player1_score = 0
# player2_score = 0

# while True:
#     input("Please press enter to roll.")
#     die1 = random.randint(1, 6)
#     die2 = random.randint(1, 6)
#     player1_score += die1
#     player1_score += die2
#     print("Player 1:", player1_score, die1)
#     print("Player 2:", player2_score, die2)
#     if player1_score > 20 or player2_score > 20:
#         winning_player = "Player 1" if player1_score > 20 else "Player 2"
#         print(f"welldone {winning_player} won")
#         break

# import datetime
# then = datetime.datetime.now()
# number_of_run = 10000
# for i in range(10):
#     while number_of_run>0:
#         (500 **i)/2
#         number_of_run -= 1
#     now = datetime.datetime.now()

#     time_taken = now - then
#     print(500 ** i, time_taken.microseconds/1000)

file = open("application_data.csv", "r")
data = file.read().split(",")
file.close()
file = open("application_data.csv", "w")

for line in data:
    print(data)