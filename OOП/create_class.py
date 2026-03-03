class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


    def show_info(self):
        print(f"Студент - {self.name} та бал - {self.grade}.")


a = Student("Олексій", "12" )
b = Student("Андрій", "20")

a.show_info()
b.show_info()