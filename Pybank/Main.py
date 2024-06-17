#Instructions:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

#Import Modules
import os 
import csv

#path to file
csvpath = os.path.join('Resources','budget_data.csv')

#open the csv
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	header = next(csvreader)

 	#Variables
	total_months = 0
	net = 0
	monthly_change = []
	previous_month_profit = 0
	greatest_increase = ["", 0]
	greatest_decrease = ["", 0]
	date = []		
	
	#Main loop
	for row in csvreader:
		total_months += 1
		net += int(row[1])
		change = int(row[1]) - previous_month_profit
		previous_month_profit = int(row[1])
		monthly_change.append(change)
		date.append(row[0])

		#calculate greatest increase and decrease
		if change > greatest_increase[1]:
			greatest_increase[0] = row[0]
			greatest_increase[1] = change
		if change < greatest_decrease[1]:
			greatest_decrease[0] = row[0]
			greatest_decrease[1] = change

	#average change
	average = sum(monthly_change) / len(monthly_change)

	#greatest increase and decrease values
	greatest_increase = max(monthly_change)
	greatest_increase_date = date[monthly_change.index(greatest_increase)]
	greatest_decrease = min(monthly_change)
	greatest_decrease_date = date[monthly_change.index(greatest_decrease)]


	#Print Results
	print("Financial Analysis")
	print("--------------------------")
	print(f"Total Months: {total_months}")
	print(f"Total: ${net}")
	print(f"Average Change: ${average}")
	print(f"Greatest Increase in Profits: {greatest_increase_date} {greatest_increase}")
	print(f"Greatest Decrease in Profits: {greatest_decrease_date} {greatest_decrease}")

	#Output to text file
	os.makedirs('Analysis', exist_ok=True)
	output = os.path.join('Analysis','Financial_Analysis.txt')
	with open(output, 'w') as textfile:
		textfile.write("Financial Analysis\n")
		textfile.write("--------------------------------\n")
		textfile.write(f"Total Months: {total_months}\n")
		textfile.write(f"Total: ${net}\n")
		textfile.write(f"Average Change: ${average}\n")
		textfile.write(f"Greatest Increase in Profits: {greatest_increase}\n")
		textfile.write(f"Greatest Decrease in Profits: {greatest_decrease}\n")





	
	











