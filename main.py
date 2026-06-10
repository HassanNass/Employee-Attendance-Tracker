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
