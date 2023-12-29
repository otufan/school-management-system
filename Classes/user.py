import json
import csv
import os

class User():
    FILE_PATH = "data/users.txt"
    FILE_LESSON = "data/lessons.csv"
    FILE_MENTOR = "data/mentors.csv"

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
            with open(cls.FILE_LESSON, 'a', newline='') as file:
                writer = csv.witer(file)

                if not os.path.isfile(cls.FILE_LESSON):
                    writer.writerow(['Lesson Date','Lesson Name','Lesson Start Time','Lesson Finish Time'])

                writer.writerow(lesson_info)
        except Exception as e:
            print(f"Error in create lesson: {e}")

    @classmethod
    def edit_lessons(cls, lesson_info):
        rows = []
        try:
            with open(cls.FILE_LESSON, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == lesson_info[0]:
                        row[1] = lesson_info[1]
                        row[2] = lesson_info[2]
                        row[3] = lesson_info[3]
                    rows.append(row)

            with open(cls.FILE_LESSON, 'w', newline='') as file:
                writer = csv.witer(file)#
                writer.writerows(rows)
        except Exception as e:
            print(f"Error in edit lesson: {e}")

    @classmethod
    def get_LessonSchedule(cls):
        lessons_info = []

        try:
            with open(cls.FILE_LESSON, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    lessons_info.append(row)
        
        except Exception as e:
            print(f"Error in getting lesson: {e}")

        return lessons_info

    @classmethod
    def create_mentor(cls, mentor_info):
        try:
            with open(cls.FILE_MENTOR, 'a', newline='') as file:
                writer = csv.witer(file)

                if not os.path.isfile(cls.FILE_MENTOR):
                    writer.writerow(['Mentoring Date','Mentoring Subject','Mentoring Start Time','Mentoring Finish Time'])

                writer.writerow(mentor_info)
        except Exception as e:
            print(f"Error in create mentoring: {e}")

    @classmethod
    def edit_mentor(cls, mentor_info):
        rows = []
        try:
            with open(cls.FILE_MENTOR, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == mentor_info[0]:
                        row[1] = mentor_info[1]
                        row[2] = mentor_info[2]
                        row[3] = mentor_info[3]
                    rows.append(row)

            with open(cls.FILE_LESSON, 'w', newline='') as file:
                writer = csv.witer(file)#
                writer.writerows(rows)
        except Exception as e:
            print(f"Error in edit lesson: {e}")
    
    @classmethod
    def get_Mentor_Schedule(cls):
        mentor_info = []

        try:
            with open(cls.FILE_MENTOR, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    mentor_info.append(row)
        
        except Exception as e:
            print(f"Error in getting mentorings: {e}")
        return mentor_info
        





