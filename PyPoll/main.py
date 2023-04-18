#%%

import csv

with open('./Resources/election_data.csv', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    ballot = []
    charles = 0
    diana = 0
    raymon = 0

    next(csv_reader)

    for row in csv_reader:
        ballot.append(row[0]) 
        
        if row[2] == 'Charles Casper Stockham':
            charles += 1
        if row[2] == 'Diana DeGette':
            diana += 1        
        if row[2] == 'Raymon Anthony Doane':
            raymon += 1

candidates = {
    'Charles Casper Stockham': charles,
    'Diana DeGette': diana,
    'Raymon Anthony Doane': raymon
}

print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(len(ballot)))
print('-------------------------')
print('Charles Casper Stockham: ' + str(round(100*charles/len(ballot), 3)) + '% (' + str(charles) + ')')
print('Diana DeGette: ' + str(round(100*diana/len(ballot), 3)) + '% (' + str(diana) + ')')
print('Raymon Anthony Doane: ' + str(round(100*raymon/len(ballot), 3)) + '% (' + str(raymon) + ')')
print('-------------------------')
print('Winner: ' + str(max(candidates, key=candidates.get)))
print('-------------------------')

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

# %%
