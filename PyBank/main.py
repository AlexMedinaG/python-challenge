#%%

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

# %%
