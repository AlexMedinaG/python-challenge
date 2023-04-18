# python-challenge

###for PyPoll
import csv

#open file as csv
with open('./Resources/election_data.csv', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

# declare starting conditions
    ballot = []
    charles = 0
    diana = 0
    raymon = 0

#skip headers
    next(csv_reader)

# for each row, count every time a name equals a different candidate
    for row in csv_reader:
        ballot.append(row[0]) 
        
        if row[2] == 'Charles Casper Stockham':
            charles += 1
        if row[2] == 'Diana DeGette':
            diana += 1        
        if row[2] == 'Raymon Anthony Doane':
            raymon += 1

#array for determining winner
candidates = {
    'Charles Casper Stockham': charles,
    'Diana DeGette': diana,
    'Raymon Anthony Doane': raymon
}

#print information to terminal
print('Election Results')
print('-------------------------')
#using len to count the list size
print('Total Votes: ' + str(len(ballot)))
print('-------------------------')
#takes the candidate and give the % by dividing the number of times the candidate name repeats by the total ballots
print('Diana DeGette: ' + str(round(100*diana/len(ballot), 3)) + '% (' + str(diana) + ')')
print('Charles Casper Stockham: ' + str(round(100*charles/len(ballot), 3)) + '% (' + str(charles) + ')') 
print('Diana DeGette: ' + str(round(100*diana/len(ballot), 3)) + '% (' + str(diana) + ')')
print('Raymon Anthony Doane: ' + str(round(100*raymon/len(ballot), 3)) + '% (' + str(raymon) + ')')
print('-------------------------')
#get the candidate with the max number of ballots, from candidates array
print('Winner: ' + str(max(candidates, key=candidates.get))) 
print('-------------------------')

#write information to text file
with open('./analysis/PyPoll.txt', 'w') as file:
    file.write('Election Results' + '\n')
    file.write('-------------------------' + '\n')
    file.write('Total Votes: ' + str(len(ballot)) + '\n')
    file.write('-------------------------' + '\n')
    file.write('Charles Casper Stockham: ' + str(round(100*charles/len(ballot), 3)) + '% (' + str(charles) + ')' + '\n')
    file.write('Diana DeGette: ' + str(round(100*diana/len(ballot), 3)) + '% (' + str(diana) + ')' + '\n')
    file.write('Raymon Anthony Doane: ' + str(round(100*raymon/len(ballot), 3)) + '% (' + str(raymon) + ')' + '\n')
    file.write('-------------------------' + '\n')
    file.write('Winner: ' + str(max(candidates, key=candidates.get)) + '\n')
    file.write('-------------------------' + '\n')



### for PyBank
import csv

#open file as csv
with open('./Resources/budget_data.csv', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

# declare starting conditions
    months = []
    profit = []
    change = 0
    change_list = []
    increase = 0
    increase_date = 0
    decrease = 0
    decrease_date = 0

#skip headers
    next(csv_reader)


    for row in csv_reader:

#for each row create a list for months and profit
        months.append(row[0]) 
        profit.append(int(row[1]))

#for each row, determine if the value is higher or lower than the "change" value; if so, save the values in row 1 and 0 to each variable
        if int(row[1]) - change > increase:
            increase = int(row[1]) - change
            increase_date = row[0]
        if int(row[1]) - change < decrease:
            decrease = int(row[1]) - change
            decrease_date = row[0]

#makes a list with the values for change
        change_list.append(int(row[1]) - change)
        change = int(row[1])

#takes out the first item from the list 
change_list.pop(0)

#print information to terminal
print('Financial Analysis')
print('----------------------------')
#count the list items to get the total months
print('Total Months: ' + str(len(months)))
#sum all profits to get the total 
print('Total: $' + str(sum(profit)))
#round the sum of all the items from the change_list and divide by the count of the items to get the average
print('Average change: $' + str(round(sum(change_list)/len(change_list), 2)))
#get the latest value for the variables in increase and decrease profits
print('Greatest Increase in Profits: ' + increase_date + ' ($' + str(increase) + ')')
print('Greatest Decrease in Profits: ' + decrease_date + ' ($' + str(decrease) + ')')

#write information to text file
with open('./analysis/PyBank.txt', 'w') as file:
    file.write('Financial Analysis' + '\n')
    file.write('----------------------------' + '\n')
    file.write('Total Months: ' + str(len(months)) + '\n')
    file.write('Total: $' + str(sum(profit)) + '\n')
    file.write('Average change: $' + str(round(sum(change_list)/len(change_list), 2)) + '\n')
    file.write('Greatest Increase in Profits: ' + increase_date + ' ($' + str(increase) + ')' + '\n')
    file.write('Greatest Decrease in Profits: ' + decrease_date + ' ($' + str(decrease) + ')')
