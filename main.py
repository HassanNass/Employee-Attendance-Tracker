# Employee Attendance Tracker

from datetime import datetime

# List that stores all employees records.
# Each employee is represented as a dictionary containing:
# - 'name': the employee's name
# - 'attendance': another dictionary where:
#	  key = date
#	  value = attendance status
# Attendance refer to : P for Present, A for Absent and L for Late
employees = [ 
	{ 
		"name": "Nass", 
		"attendance": { 
			"2026-06-01": "P", 
			"2026-06-02": "P", 
			"2026-06-03": "A", 
			"2026-06-04": "L"
			}
    },
	{ 
		"name": "Bob", 
		"attendance": { 
			"2026-06-01": "L", 
			"2026-06-02": "P", 
			"2026-06-03": "A", 
			"2026-06-04": "P"
		}
	}
]


# Register a new employee in the system
# Prevents duplicate employee names
def register_employee(employees):

	# Ask the user for the employee's and remove extra whitespaces
	name = input("Enter employee name: ").strip()

	# Check if an employee with the same name already exists (case-insensitive)
	for employee in employees:
		if employee['name'].lower() == name.lower():
			print("An employee with that name already exists!")
			print("\n")
			return
	
	# Add the new employee with an empty attendance record
	employees.append({"name": name, "attendance": {}})
	print(f"Record registered successfully, with the name of {name}.")
	print("\n")


# Allows the user to enter a date and attendance status
# Prevents overwriting attendance records that already exists
def record_attendance(employees):

	# Ask for the employee's name and remove extra whitespaces
	name = input("Enter the name: ").strip()

	# Search for the employee by name (case-insensitive)
	for employee in employees:
		if employee['name'].lower() == name.lower():

			# Keep asking for a date until a valid one is entered or the user types DONE to cancel
			while True:
				# Ask for the attendance date and remove extra whitespaces
				date = input("Enter the date (YYYY-MM-DD): ").strip()

				# Allow the user to cancel attendance recording
				if date.upper() == "DONE":
					return
				
				try:
					# Validate that the date follows the YYYY-MM-DD format
					parsed = datetime.strptime(date, "%Y-%m-%d")

					# If it follows the correct format, set leading zeros
					date = parsed.strftime("%Y-%m-%d")
					break

				except ValueError:
					# Runs when the entered date is invalid
					print("Invalid date! Please use the format YYYY-MM-DD or type 'Done' to cancel.")

			# Prevent duplicate attendance entries for the same date
			if date in employee['attendance']:
				print("Attendance for that date already exists. No overwriting!")
				return
			
			# Ask for the attendance status and remove extra whitespaces and convert it to uppercase
			status = input("Enter status (P / A / L): ").strip().upper()

			# Keep asking until a valid status is entered or the user types DONE to cancel
			while status not in ["P", "A", "L"]:
				print("Invalid status! Please enter P, A or L - or type 'Done' to cancel.")
				status = input("Enter status (P / A / L): ").strip().upper()
				
				if status == "DONE":
					return
			
			# Add the attendance record
			employee['attendance'][date] = status
			
			print(f"Attendance recorded: {employee['name']} - {date} - {status}")
			return

	# If no employee with the given name was found, display	a message about that
	print("Employee not found.")


# Generate and display an attendance report for all employees
def generate_report(employees):

	# Dictionary used to translate attendance codes into meaningful words
	labels = {"P": "Present", "A": "Absent", "L": "Late"}

	print("\n--- Attendance Report ---")

	# Loop through every employee in the system
	for employee in employees:

		# Display the employee's name
		print(f"\n{employee['name']}")

		# Check if the employee has any attendance records
		if not employee['attendance']:
			print(" No attendance records found.")
			continue

		# Loop through each attendance using item() that return key-value pairs
		for date, status in employee['attendance'].items():

			# Print the date and its label
			print(f" {date} : {labels[status]}")


# Calculate attendance satistics for a single employee
def calculate_stats(employee):

	# Counters for each attendance status
	p_count = 0
	a_count = 0
	l_count = 0

	# Loop through all attendance statuses
	# .values() returns only the values from the attendance dictionary
	for attendance in employee['attendance'].values():

		# Count Present records
		if attendance == "P":
			p_count += 1

		# Count Absent records
		elif attendance == "A":
			a_count += 1
		
		# Any remaining valid status is considered Late
		else:
			l_count += 1

	# Total number of attendance records
	total = len(employee['attendance'])

	# Avoid division by zero if no attendance records exist
	if total == 0:
		percentage = 0.0

	# Calculate attendance percentage
	else:
		percentage = (p_count / total) * 100

	# Return all calculated statistics as a tuple
	return p_count, a_count, l_count, percentage


# Display attendance statistics for all employees.
# Show the number of Present, Absent, and Late records,
# along with the attendance percentage for each employee.
def display_statistics(employees):
	print("\n--- Attendance Statistics ---")

	# Loop through all employees and calculate their statistics
	for employee in employees:

		# Retrieve attendance statistics from calculate_stats()
		p, a, l, percentage = calculate_stats(employee)

		print(f"\n{employee['name']}")
		print(f"  Present: {p}, Absent: {a}, Late: {l}")
		print(f"  Attendance percentage: {percentage:.2f}%")

