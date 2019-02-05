import os
import csv
import string

with open('Resources/budget_data.csv', newline='') as finRecords:
    csvreader = csv.reader(finRecords, delimiter=',')
    csv_header = next(csvreader) # Skip the header
        
# Read each row of data and find the
#  * The total number of months included in the dataset
#  * The net total amount of "Profit/Losses" over the entire period
#  * The average of the changes in "Profit/Losses" over the entire period
#  * The greatest increase in profits (date and amount) over the entire period
#  * The greatest decrease in losses (date and amount) over the entire period

    row = next(csvreader)
    nMonths = 1
    profit =int(row[1])
    netProfitOrLoss = int(row[1])
    greatestIncreaseInProfitAmount = int(row[1])
    greatestIncreaseInProfitsDate = row[0]
    greatestDecreaseInProfitAmount = int(row[1])
    greatestDecreaseInProfitsDate = row[0]
    averageChange = 0
    for row in csvreader:
        diffProfit = int(row[1]) - profit
        if (diffProfit > greatestIncreaseInProfitAmount):
            greatestIncreaseInProfitAmount = diffProfit
            greatestIncreaseInProfitsDate = row[0]
        elif (diffProfit < greatestDecreaseInProfitAmount):
            greatestDecreaseInProfitAmount = diffProfit
            greatestDecreaseInProfitsDate = row[0]
        nMonths = nMonths + 1
        profit =int(row[1])
        netProfitOrLoss = netProfitOrLoss + int(row[1])
        averageChange = averageChange + diffProfit
    
averageChange = averageChange/(nMonths-1)

print("  Financial Analysis ")
print("  ----------------------------")
print("  Total Months: %d "% nMonths )
print("  Total: $%10.2f"% netProfitOrLoss)
print("  Average  Change: $%10.2f"% averageChange)
print(f'  Greatest Increase in Profits: {greatestIncreaseInProfitsDate} ({greatestIncreaseInProfitAmount})')
print(f'  Greatest Increase in Profits: {greatestDecreaseInProfitsDate} ({greatestDecreaseInProfitAmount})')

# Write results to new txt file

file = open('Resources/PyBankAnalysis.txt','w') 
file.write("  Financial Analysis \r\n")
file.write("  ----------------------------\r\n")
file.write("  Total Months: %d\r\n"% nMonths )
file.write("  Total: $%d\r\n"% netProfitOrLoss)
file.write("  Average  Change: $%d\r\n" % averageProfitOrLoss)
file.write(f'  Greatest Increase in Profits: {greatestIncreaseInProfitsDate} ({greatestIncreaseInProfitAmount})\r\n')
file.write(f'  Greatest Increase in Profits: {greatestDecreaseInProfitsDate} ({greatestDecreaseInProfitAmount})\r\n')

file.close()
