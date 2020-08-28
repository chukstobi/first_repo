import csv

csv_file = csv.reader(open('E0.csv'))
next(csv_file)
upsets = 0
non_upsets = 0

starting_bankroll = 100
wagering_size = 5

bankroll = starting_bankroll

for game in csv_file:
    home_team = game[3]
    away_team = game[4]
    home_team_goals = int(game[5])
    away_team_goals = int(game[6])
    home_team_odds = float(game[26])
    draw_odds = float(game[27])
    away_team_odds = float(game[28])
    if home_team_odds > away_team_odds:
        if home_team_goals > away_team_goals:
            upsets +=1
            bankroll +=wagering_size * (home_team_odds-1)
        else:
            non_upsets+=1
            bankroll-=wagering_size

print(bankroll)
