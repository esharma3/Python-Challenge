
import csv
import os
from datetime import datetime
from US_States import *


in_filepath = os.path.join("Input & Output","employee_data.csv")
out_filepath = os.path.join("Input & Output","formatted_employee_data.csv")


with open(in_filepath, "r", newline ="") as in_file:

	reader = csv.DictReader(in_file)

	with open(out_filepath, "w", newline = "") as out_file:

		fieldnames = ['Employee ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']

		writer = csv.DictWriter(out_file, fieldnames=fieldnames, delimiter = ',')

		# Writing the output header before we start writing the data rows		
		writer.writeheader()

				
		for row in reader:
			
			Emp_ID = row['Emp ID']

			# Formatting the name 
			First_Name, Last_Name = row['Name'].split(" ", 1) # will return a list of 2 elements

			# Formatting the DOB 
			frmt_date = datetime.strptime(row['DOB'], "%Y-%m-%d")
			dob = frmt_date.strftime("%m/%d/%Y")
			
			# Formatting the SSN
			ssn = "***-**-" + row['SSN'][7:]

			# Formatting the State to get abbreviated state (.strip is used to strip away \n(s) from the end of each row)
			State = row['State'].strip()  
			Abbrev_State = us_state_abbrev.get(State)
			
            # Writing the formatted data to the output file
			writer.writerow({'Employee ID': Emp_ID, 'First Name': First_Name, 'Last Name': Last_Name, 'DOB': dob, 'SSN': ssn, 'State': Abbrev_State})



 
