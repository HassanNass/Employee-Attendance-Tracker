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

