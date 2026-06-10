# Employee Attendance Tracker

A command-line employee attendance management system built in Python. Supports registering employees, recording daily attendance with date validation, generating attendance reports, and displaying statistics for each employee.

---

## Features

### Employee Management
- Register new employees with duplicate name prevention (case-insensitive)

### Attendance Recording
- Record attendance by employee name and date
- Date validation — only accepts the `YYYY-MM-DD` format
- Attendance codes: **P** (Present), **A** (Absent), **L** (Late)
- Prevents overwriting existing attendance records for the same date
- Type `DONE` at any prompt to cancel and return to the menu

### Reports
- Generate a full attendance report for all employees
- Displays each date and its corresponding attendance status in a readable format

### Statistics
- Displays the total number of Present, Absent, and Late records per employee
- Calculates and displays the attendance percentage for each employee

---

## How to Run

Make sure you have Python 3 installed.

```bash
python attendance.py
```

---

## Example

```
--- Employee Attendance Tracker ---
1. Register employee
2. Record attendance
3. Generate report
4. Display statistics
5. Exit
Enter your choice (1-5): 3

--- Attendance Report ---

Nass
 2026-06-01 : Present
 2026-06-02 : Present
 2026-06-03 : Absent
 2026-06-04 : Late

Bob
 2026-06-01 : Late
 2026-06-02 : Present
 2026-06-03 : Absent
 2026-06-04 : Present
```

---

## Project Structure

```
Employee-Attendance-Tracker/
├── attendance.py
└── README.md
```

---

## What I Practiced

- Working with nested data structures — lists of dictionaries where each dictionary contains another dictionary
- Date validation using Python's `datetime.strptime`
- Separating logic from display — `calculate_stats` computes the data, `display_statistics` handles the output
- Returning multiple values from a function using tuples
- Building a multi-option CLI menu with clean input handling and cancellation support

---

## Author

**Hassan Nasrallah**
[github.com/HassanNass](https://github.com/HassanNass)
