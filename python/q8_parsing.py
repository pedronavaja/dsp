# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
with open('football.csv') as csvfile:
    football = csv.reader(csvfile, delimiter = ',')

    for_against = []

    football.next()

    for line in football:
        goals = (line[0],int(line[5]),int(line[6]))
        for_against.append(goals)

    print(min(for_against, key = lambda t: abs(t[1] - t[2])))

csvfile.close()
