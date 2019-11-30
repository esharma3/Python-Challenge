
import os
import csv


revenue, change_in_revenue, date = [], [], []
total_revenue = 0
count = 0


in_filepath = os.path.join('Input & Output', 'budget_data.csv') 
out_filepath = os.path.join('Input & Output', 'budget_data_analysis.csv')


with open(in_filepath, newline = '') as in_file: 

	reader = csv.reader(in_file, delimiter=',')
	header = next(reader)


	# Calculating total number of months by counting the number of rows in the csv file 
	# Adding Profit/Loss to revenue list & dates to date list 
	for row in reader:

		count += 1

		revenue.append(row[1]) 
		date.append(row[0]) 
	

	# Calculating the total amount of Profit/Losses
	for i in range(0, count):
		total_revenue += int(revenue[i])


	# Calculating increase/decrease in revenue and adding it to change_in_revenue list	# Calculating the average of changes 
	for i in range(0, count-1):
		change_in_revenue.append(int(revenue[i+1]) - int(revenue[i]))

	avg_of_changes = round(sum(change_in_revenue)/(count - 1), 2)

	
	# Calculating the greatest increase and greatest decrease (min_increase) in profilt/loss changes
	max_increase = change_in_revenue[0]
	min_increase = change_in_revenue[0]

	for j in range(1, count-1):
		
		if max_increase < int(change_in_revenue[j]):
			max_increase = int(change_in_revenue[j])
			related_date1 = date[j+1] 

		if min_increase > int(change_in_revenue[j]):
			min_increase = int(change_in_revenue[j])
			related_date2 = date[j+1]


summary = (
	"Financial Analysis\n"
	"---------------------\n"
	f"Total Months: {count}\n"
	f"Total: ${total_revenue}\n"	
	f"Average Change: ${avg_of_changes}\n"	
	f"Greatest Increase in Profits: {related_date1} (${max_increase})\n"
	f"Greatest Decrease in Profits: {related_date2} (${min_increase})"
	)

# Printing output to the terminal  
print(summary)

# Writing output to the file
with open(out_filepath, 'w+', newline = '') as out_text:
	out_text.write(summary)



	



