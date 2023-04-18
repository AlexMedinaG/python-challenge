#%%

import csv

with open('./Resources/budget_data.csv', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    months = []
    profit = []
    change = 0
    change_list = []
    increase = 0
    increase_date = 0
    decrease = 0
    decrease_date = 0

    next(csv_reader)

    for row in csv_reader:
        months.append(row[0]) 
        profit.append(int(row[1]))

        if int(row[1]) - change > increase:
            increase = int(row[1]) - change
            increase_date = row[0]
        if int(row[1]) - change < decrease:
            decrease = int(row[1]) - change
            decrease_date = row[0]

        change_list.append(int(row[1]) - change)

        change = int(row[1])

change_list.pop(0)
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(len(months)))
print('Total: $' + str(sum(profit)))
print('Average change: $' + str(round(sum(change_list)/len(change_list), 2)))
print('Greatest Increase in Profits: ' + increase_date + ' ($' + str(increase) + ')')
print('Greatest Decrease in Profits: ' + decrease_date + ' ($' + str(decrease) + ')')

with open('./analysis/PyBank.txt', 'w') as file:
    file.write('Financial Analysis' + '\n')
    file.write('----------------------------' + '\n')
    file.write('Total Months: ' + str(len(months)) + '\n')
    file.write('Total: $' + str(sum(profit)) + '\n')
    file.write('Average change: $' + str(round(sum(change_list)/len(change_list), 2)) + '\n')
    file.write('Greatest Increase in Profits: ' + increase_date + ' ($' + str(increase) + ')' + '\n')
    file.write('Greatest Decrease in Profits: ' + decrease_date + ' ($' + str(decrease) + ')')

# %%
