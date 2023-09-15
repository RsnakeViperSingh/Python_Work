#write a code to dispaly the grade of a student ...

class Student:
    def _init_(self):
        self.marks = []

    def read_marks(self):
        for i in range(5):
            mark = int(input(f"Enter marks for subject {i+1}: "))
            self.marks.append(mark)

    def calculate_percentage(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / 500) * 100
        return percentage

    def calculate_grade(self, percentage):
        if percentage >= 90 and percentage <= 100:
            return "M"
        elif percentage >= 60 and percentage <= 89:
            return "First"
        elif percentage >= 50 and percentage <= 59:
            return "Second"
        elif percentage >= 35 and percentage <= 49:
            return "3rd"
        else:
            return "Fail"

    def display_result(self):
        percentage = self.calculate_percentage()
        grade = self.calculate_grade(percentage)
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")


student = Student()
student.read_marks()
student.display_result()
