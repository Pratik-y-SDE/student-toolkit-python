# -*- coding: utf-8 -*-
"""
GPA Calculator
--------------
Calculates SGPA (Semester GPA) and CGPA (Cumulative GPA)
based on subject grades and credit hours.
"""

GRADE_POINTS = {
    'O':  10,   # Outstanding
    'A+':  9,
    'A':   8,
    'B+':  7,
    'B':   6,
    'C':   5,
    'P':   4,   # Pass
    'F':   0,   # Fail
    'AB':  0,   # Absent
}

def display_grade_table():
    print("\n  Grade Scale:")
    print("  " + "-" * 30)
    print(f"  {'Grade':<10} {'Grade Points':<12}")
    print("  " + "-" * 30)
    for grade, points in GRADE_POINTS.items():
        print(f"  {grade:<10} {points:<12}")
    print("  " + "-" * 30)

def get_valid_grade():
    while True:
        grade = input("    Grade (O/A+/A/B+/B/C/P/F): ").strip().upper()
        if grade in GRADE_POINTS:
            return grade
        print("    [!] Invalid grade. Please enter a valid grade from the table.")

def get_positive_float(prompt, max_val=None):
    """Get a positive float, optionally bounded by max_val."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("    [!] Value must be greater than 0.")
                continue
            if max_val is not None and value > max_val:
                print(f"    [!] Value cannot exceed {max_val}.")
                continue
            return value
        except ValueError:
            print("    [!] Please enter a valid number.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("    [!] Value must be a positive integer.")
        except ValueError:
            print("    [!] Please enter a valid integer.")

def calculate_sgpa():
    print("\n" + "=" * 50)
    print("         SGPA CALCULATOR (Single Semester)")
    print("=" * 50)

    display_grade_table()

    n = get_positive_int("\n  How many subjects this semester? ")
    subjects = []

    for i in range(1, n + 1):
        print(f"\n  Subject {i}:")
        name    = input("    Subject name: ").strip() or f"Subject {i}"
        credits = get_positive_float("    Credit hours : ")
        grade   = get_valid_grade()
        subjects.append((name, credits, grade))

    total_credits      = sum(c for _, c, _ in subjects)
    total_grade_points = sum(c * GRADE_POINTS[g] for _, c, g in subjects)
    sgpa               = total_grade_points / total_credits

    print("\n" + "=" * 50)
    print("               RESULT SUMMARY")
    print("=" * 50)
    print(f"  {'Subject':<20} {'Credits':<10} {'Grade':<8} {'Points'}")
    print("  " + "-" * 46)
    for name, credits, grade in subjects:
        pts = credits * GRADE_POINTS[grade]
        print(f"  {name:<20} {credits:<10.1f} {grade:<8} {pts:.1f}")
    print("  " + "-" * 46)
    print(f"  {'Total':<20} {total_credits:<10.1f} {'':8} {total_grade_points:.1f}")
    print(f"\n  >>> SGPA : {sgpa:.2f} / 10.00")

    if sgpa >= 9:
        remark = "Outstanding [****]"
    elif sgpa >= 8:
        remark = "Excellent [***]"
    elif sgpa >= 7:
        remark = "Very Good [**]"
    elif sgpa >= 6:
        remark = "Good [*]"
    elif sgpa >= 4:
        remark = "Satisfactory"
    else:
        remark = "Needs Improvement"

    print(f"  >>> Remark: {remark}")
    print("=" * 50, flush=True)

    return sgpa, total_credits

def calculate_cgpa():
    print("\n" + "=" * 50)
    print("         CGPA CALCULATOR (Multiple Semesters)")
    print("=" * 50)

    num_semesters = get_positive_int("\n  How many semesters completed? ")
    semester_data = []

    for i in range(1, num_semesters + 1):
        print(f"\n  Semester {i}:")
        # FIX: SGPA is bounded 0-10
        sgpa    = get_positive_float(f"    SGPA for Semester {i} (0-10): ", max_val=10.0)
        credits = get_positive_float(f"    Total credits              : ")
        semester_data.append((i, sgpa, credits))

    total_weighted = sum(sgpa * credits for _, sgpa, credits in semester_data)
    total_credits  = sum(credits for _, _, credits in semester_data)
    cgpa           = total_weighted / total_credits

    print("\n" + "=" * 50)
    print("               CGPA SUMMARY")
    print("=" * 50)
    print(f"  {'Semester':<12} {'SGPA':<10} {'Credits'}")
    print("  " + "-" * 32)
    for sem, sgpa, credits in semester_data:
        print(f"  {sem:<12} {sgpa:<10.2f} {credits:.1f}")
    print("  " + "-" * 32)
    print(f"\n  >>> CGPA : {cgpa:.2f} / 10.00")
    print("=" * 50, flush=True)

def run():
    while True:
        print("\n+------------------------------+")
        print("|       GPA CALCULATOR         |")
        print("+------------------------------+")
        print("|  1. Calculate SGPA           |")
        print("|  2. Calculate CGPA           |")
        print("|  3. Back to Main Menu        |")
        print("+------------------------------+", flush=True)

        choice = input("\n  Enter choice (1-3): ").strip()

        if choice == '1':
            calculate_sgpa()
        elif choice == '2':
            calculate_cgpa()
        elif choice == '3':
            break
        else:
            print("  [!] Invalid choice.")
