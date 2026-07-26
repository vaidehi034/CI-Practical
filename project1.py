import csv
import os
from datetime import datetime

FILE_NAME = "student_attendance.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Student ID",
                "Student Name",
                "Roll Number",
                "Age",
                "Gender",
                "Course",
                "Semester",
                "Phone Number",
                "Email",
                "Date",
                "Attendance Status"
            ])

def mark_attendance():
    print("\n========== Student Details ==========")

    student_id = input("Student ID: ")
    student_name = input("Student Name: ")
    roll_no = input("Roll Number: ")
    age = input("Age: ")
    gender = input("Gender: ")
    course = input("Course: ")
    semester = input("Semester: ")
    phone = input("Phone Number: ")
    email = input("Email: ")

    print("\n========== Attendance ==========")

    while True:
        status = input("Attendance (Present/Absent): ").capitalize()
        if status in ["Present", "Absent"]:
            break
        print("Please enter Present or Absent.")

    date = datetime.now().strftime("%d-%m-%Y")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            student_id,
            student_name,
            roll_no,
            age,
            gender,
            course,
            semester,
            phone,
            email,
            date,
            status
        ])

    print("\nAttendance Recorded Successfully!")

def view_records():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    print("\n============= Student Attendance Records =============\n")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

def main():
    create_file()

    while True:
        print("\n========== STUDENT ATTENDANCE SYSTEM ==========")
        print("1. Mark Attendance")
        print("2. View Attendance Records")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            view_records()

        elif choice == "3":
            print("Thank You!")
            break

        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    main()