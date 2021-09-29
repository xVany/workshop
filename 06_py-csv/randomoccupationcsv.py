'''
Trio of Success: Raymond Yeung, Annabel Zhang, Thomas Yu
SoftDev
K06: Random Occupations With Weighted Probability
2021-09-28
Summary:
 First we used DictReader to read the csv file and then iterated through it
 into a dictionary. Then we looked at the probabilities of each job by
 iterating through the dictionary and then using a randomly generated
 number between 0 and 99.8. We treated the percentage as the how big
 the interval between the two numbers are. It doesn't matter where the interval
 is, it just matters the size of the interval. If the random number falls in
 between that interval we returned the corresponding job.
'''


import random
import csv

occupations = {}

with open("occupations.csv", newline='') as csvfile:
    file = csv.DictReader(csvfile)
    for lines in file:
        occupations[lines['Job Class']] = float(lines['Percentage'])

ranNum = random.random() * 99.8
lower = 0
upper = 0

for job, percentage in occupations.items():
    lower = upper
    upper += percentage
    if lower <= ranNum < upper:
        print(job)
    
