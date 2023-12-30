import json
from PyQt5.QtWidgets import QMessageBox

class User():
    FILE_PATH = "C:/Users/MainUser/Desktop/tech_groupproject/school-management-system/data/users.txt"

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
        # Check if the email already exists
        if cls.email_exists(email):
           QMessageBox.information(None, 'Warning', f'The email {email} already exists.', QMessageBox.Ok)
            
        else:
            new_user = cls(name, surname, email, birthdate, city, phone_number, password, user_type)
            cls.save_user(new_user.__dict__)
            # Show a success message
            QMessageBox.information(None, 'Success', 'User created successfully.', QMessageBox.Ok)
        
    @classmethod
    def email_exists(cls, email):
        existing_emails = cls.get_emails_for_task_assign()
        return email in existing_emails
    
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
    
    @classmethod
    def login(cls, email, password):
        try:
            with open(cls.FILE_PATH, 'r') as file:
                for line in file:
                    user_data = json.loads(line)
                    if user_data.get('email') == email and user_data.get('password') == password:
                        return user_data
        except Exception as e:
            print(f"Error reading user data from file: {e}")
        return None

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