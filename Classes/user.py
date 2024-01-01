import json
import csv
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

class User():
    FILE_PATH = "data/users.txt"
    FILE_LESSON = "data/lessons.csv"
    FILE_MENTOR = "data/mentors.csv"
    table_lesson = None
    table_mentoring = None

    def __init__(self, name, surname, email, birthdate, city, phone_number, password, user_type):
        self.name = name
        self.surname = surname
        self.email = email
        self.birthdate = birthdate
        self.city = city
        self.phone_number = phone_number
        self.password = password
        self.user_type = user_type

    @classmethod
    def create_user(cls, name, surname, email, birthdate, city, phone_number, password, user_type):
        new_user = cls(name, surname, email, birthdate, city, phone_number, password, user_type)
        cls.save_user(new_user.__dict__)

    @classmethod
    def save_user(cls, user):
        try:
            with open(cls.FILE_PATH, 'a') as file:
                # Append the user data to the JSON file
                json.dump(user, file)
                file.write('\n')
            print("User saved to file.")
        except Exception as e:
            print(f"Error saving user to file: {e}")

    @classmethod
    def get_emails_for_task_assign(cls):
        emails = []
        try:
            with open(cls.FILE_PATH, 'r') as file:
                for line in file:
                    user_data = json.loads(line)
                    emails.append(user_data.get('email'))
        except Exception as e:
            print(f"Error reading emails from file: {e}")
        return emails

# Save the user information to the file
# User.create_user(
#     name="Student",
#     surname="Test",
#     email="student@example.com",
#     birthdate="1990-01-01",
#     city="Ist",
#     phone_number="123-456-7890",
#     password="12345",
#     user_type="student"
# )
    
    @classmethod
    def create_lessons(cls, lesson_info):
        try:
            rows = []
            flag = True

            if len(lesson_info) >= 4:
                with open(cls.FILE_LESSON, 'r', newline='') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row and row[0] == lesson_info[0]:
                            row[1] = lesson_info[1]
                            row[2] = lesson_info[2]
                            row[3] = lesson_info[3]
                            flag = False
                        rows.append(row)
                    
                    if flag:
                        rows.append(lesson_info)
                
                with open(cls.FILE_LESSON, 'w', newline='') as file:
                    writer = csv.writer(file)

                    if not os.path.isfile(cls.FILE_LESSON):
                        writer.writerow(['Lesson Date','Lesson Name','Lesson Start Time','Lesson Finish Time'])
                    writer.writerows(rows)

        except Exception as e:
            print(f"Error in create lesson: {e}")


    @classmethod
    def get_LessonSchedule(cls):
        if cls.table_lesson is None: 
            cls.table_lesson = QTableWidget()
            cls.table_lesson.setColumnCount(4)

        try:
            with open(cls.FILE_LESSON, 'r', newline='') as file:
                reader = csv.reader(file)
                cls.table_lesson.setRowCount(0)
                row_number = 0

                for row in reader:
                    cls.table_lesson.insertRow(row_number)
                    for column_number, info in enumerate(row):
                        cls.table_lesson.setItem(row_number, column_number, QTableWidgetItem(info))
                    row_number += 1
        
        except Exception as e:
            print(f"Error in getting lesson: {e}")

        return cls.table_lesson

    @classmethod
    def create_mentor(cls, mentor_info):
        try:
            rows = []
            flag = True
            if len(mentor_info) >= 4:
                with open(cls.FILE_MENTOR, 'r', newline='') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row and row[0] == mentor_info[0]:
                            row[1] = mentor_info[1]
                            row[2] = mentor_info[2]
                            row[3] = mentor_info[3]
                            flag = False
                        rows.append(row)
                    
                    if flag:
                        rows.append(mentor_info)
                
                with open(cls.FILE_MENTOR, 'w', newline='') as file:
                    writer = csv.writer(file)

                    if not os.path.isfile(cls.FILE_MENTOR):
                        writer.writerow(['Mentoring Date','Mentoring Subject','Mentoring Start Time','Mentoring Finish Time'])
                    writer.writerows(rows)

        except Exception as e:
            print(f"Error in create mentoring: {e}")

    
    @classmethod
    def get_Mentor_Schedule(cls):
        if cls.table_mentoring is None: 
            cls.table_mentoring = QTableWidget()
            cls.table_mentoring.setColumnCount(4)

        try:
            with open(cls.FILE_MENTOR, 'r', newline='') as file:
                reader = csv.reader(file)
                cls.table_mentoring.setRowCount(0)
                row_number = 0

                for row in reader:
                    cls.table_mentoring.insertRow(row_number)
                    for column_number, info in enumerate(row):
                        cls.table_mentoring.setItem(row_number, column_number, QTableWidgetItem(info))
                    row_number += 1
        
        except Exception as e:
            print(f"Error in getting lesson: {e}")

        return cls.table_mentoring
    
        




