"""
Gradebook Analyzer
Author: Archita
Date: 27-Nov-2025
Description:
A simple command-line program to collect student marks (manual or CSV),
compute basic statistics, assign letter grades, show pass/fail lists,
and print a final results table.
"""

import csv
import statistics

# Statistics Analysis Function
def calculate_average(marks_dict):
    if not marks_dict:
        return 0.0
    total = sum(marks_dict.values())
    avg = total / len(marks_dict)
    return round(avg, 2)

def calculate_median(marks_dict):
    if not marks_dict:
        return 0.0
    return statistics.median(list(marks_dict.values()))

def find_max_score(marks_dict):
    return max(marks_dict.values()) if marks_dict else None

def find_min_score(marks_dict):
    return min(marks_dict.values()) if marks_dict else None

# Grade assignment
def assign_grades(marks_dict):
    """ A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60 """
    grades = {}
    counts = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for name, mark in marks_dict.items():
        if mark >= 90:
            letter = "A"
        elif mark >= 80:
            letter = "B"
        elif mark >= 70:
            letter = "C"
        elif mark >= 60:
            letter = "D"
        else:
            letter = "F"
        grades[name] = letter
        counts[letter] += 1
    return grades, counts

# Pass/Fail list
def pass_fail_lists(marks_dict):
    """ Using list comprehension:
    passed_students = score >= 40
    failed_students = score < 40 """
    passed = [s for s, m in marks_dict.items() if m >= 40]
    failed = [s for s, m in marks_dict.items() if m < 40]
    return passed, failed

# Input enteries
def manual_entry():
    marks = {}
    while True:
        try:
            n = int(input("How many students to enter? (e.g., 5): ").strip())
            if n <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid number. Try again.")
    for i in range(1, n+1):
        name = input(f"Enter name for student {i}: ").strip()
        while True:
            try:
                mark = float(input(f"Enter marks (0-100) for {name}: ").strip())
                if mark < 0 or mark > 100:
                    print("Please enter marks between 0 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid mark. Enter a number like 78 or 92.5.")
        marks[name] = mark
    return marks

def csv_entry():
    marks = {}
    filename = input("Enter CSV filename (e.g., students.csv): ").strip()
    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                # name,marks
                name = row[0].strip()
                try:
                    mark = float(row[1].strip())
                except (IndexError, ValueError):
                    print(f"Skipping invalid row: {row}")
                    continue
                marks[name] = mark
        print(f"Loaded {len(marks)} students from '{filename}'.")
    except FileNotFoundError:
        print("File not found. Make sure the file is in the same folder as this script.")
    except Exception as e:
        print("Error reading CSV:", e)
    return marks

# Output 
def print_results_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-" * 36)
    for name, mark in marks.items():
        name_disp = name if len(name) < 8 else name[:8]
        print(f"{name_disp:8}\t{mark:5}\t{grades[name]}")
    print("-" * 36)

def export_to_csv(marks, grades):
    choice = input("Do you want to save the results to CSV? (y/n): ").strip().lower()
    if choice != 'y':
        return
    out_name = input("Enter output filename (e.g., results.csv): ").strip()
    try:
        with open(out_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Marks", "Grade"])
            for name, mark in marks.items():
                writer.writerow([name, mark, grades[name]])
        print(f"Results saved to '{out_name}'.")
    except Exception as e:
        print("Could not write CSV:", e)

# Main 
def main():
    print("Welcome to Gradebook Analyzer")
    while True:
        print("\nChoose input method:")
        print("  1 - Manual entry (type student names & marks)")
        print("  2 - Load from CSV file (name,marks)")
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            marks = manual_entry()
        elif choice == "2":
            marks = csv_entry()
        else:
            print("Please enter 1 or 2.")
            continue

        if not marks:
            print("No student data available. Returning to menu.")
            continue

        # compute stats
        avg = calculate_average(marks)
        med = calculate_median(marks)
        mx = find_max_score(marks)
        mn = find_min_score(marks)

        print("\n--- Statistical Summary ---")
        print(f"Average marks: {avg}")
        print(f"Median marks: {med}")
        print(f"Highest mark: {mx}")
        print(f"Lowest mark: {mn}")

        # grades
        grades, grade_counts = assign_grades(marks)
        print("\n--- Grade Distribution ---")
        for g in ["A","B","C","D","F"]:
            print(f"{g}: {grade_counts[g]} student(s)")

        # pass/fail
        passed, failed = pass_fail_lists(marks)
        print(f"\nPassed students ({len(passed)}): {', '.join(passed) if passed else 'None'}")
        print(f"Failed students ({len(failed)}): {', '.join(failed) if failed else 'None'}")

        # results table
        print_results_table(marks, grades)

        # export CSV
        export_to_csv(marks, grades)

        again = input("\nDo you want to analyze another set? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting. Good luck! — Gradebook Analyzer")
            break

if __name__ == "__main__":
    main()
