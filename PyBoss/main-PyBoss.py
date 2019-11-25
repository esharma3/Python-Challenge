
import csv
import os
from datetime import datetime
from US_States import *


in_filepath = os.path.join("Input & Output","employee_data.csv")
out_filepath = os.path.join("Input & Output","formatted_employee_data.csv")


with open(out_filepath, "w+", newline ="") as out_text:
	with open(in_filepath, "r") as in_text:

		reader = csv.reader(in_text)
		writer = csv.writer(out_text)

		# Writing the output header before we start writing the data rows
		out_header = ['Employee_ID', 'First_Name', 'Last_Name', 'DOB', 'SSN', 'State']
		writer.writerow(out_header)

		# Pops the input header row 
		in_header = next(in_text) 
		

		for row in reader:
			
			Emp_ID = row[0]

			# Formatting the name 
			First_Name, Last_Name = row[1].split(" ", 1) # will return a list of 2 elements

			# Formatting the DOB 
			frmt_date = datetime.strptime(row[2], "%Y-%m-%d")
			DOB = frmt_date.strftime("%m/%d/%Y")
			
			# Formatting the SSN
			SSN = "***-**-" + row[3][7:]

			# Formatting the Sate to get abbreviated state (.strip is used to strip away \n(s) from the end of each row)
			State = row[4].strip()  
			Abbrev_State = us_state_abbrev.get(State)
			
            # Writing the formatted data to the output file
			writer.writerow([Emp_ID, First_Name, Last_Name, DOB, SSN, Abbrev_State])



 
