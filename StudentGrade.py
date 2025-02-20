import os

class GradeManager:
    def __init__(self, filename="grades.txt"):
        self.filename = filename

    def add_default_students(self):
        """Adds five default student records to the file."""
        students = [
            ("1001", "Alice Johnson", "Mathematics", "A"),
            ("1002", "Bob Smith", "Physics", "B+"),
            ("1003", "Charlie Brown", "Chemistry", "A-"),
            ("1004", "Daisy Miller", "English", "B"),
            ("1005", "Ethan Davis", "History", "A"),
        ]

        try:
            with open(self.filename, "w") as file:  # Overwrite the file with default students
                for student in students:
                    file.write(",".join(student) + "\n")
            print("Default student records added successfully.")
        except PermissionError:
            print(f"Error: Permission denied to write to {self.filename}")
        except Exception as e:
            print(f"Unexpected error while writing to file: {e}")

    def view_grades(self):
        """Reads and displays all student grades from the file."""
        try:
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"Error: The file '{self.filename}' does not exist.")

            with open(self.filename, "r") as file:
                records = file.readlines()

            if not records:
                print("No student records found.")
                return []

            print("\nStudent Grades:")
            print("ID   | Name          | Subject       | Grade")
            print("---------------------------------------------")
            for record in records:
                student_data = record.strip().split(",")
                print(f"{student_data[0]:<4} | {student_data[1]:<12} | {student_data[2]:<14} | {student_data[3]}")
            
            return records
        except FileNotFoundError as e:
            print(e)
            return []
        except PermissionError:
            print(f"Error: Permission denied to read the file '{self.filename}'")
            return []
        except Exception as e:
            print(f"Unexpected error while reading file: {e}")
            return []

def main():
    manager = GradeManager()

    # Adding 5 default students
    manager.add_default_students()

    # Displaying student grades
    manager.view_grades()

if __name__ == "__main__":
    main()
