class User:
    def __init__(self, name):
        print("User.__init__ called.")
        self.name = name
    
    def log_in(self):
        print("User.log_in() called.")
        self.logged_in = True

class Student(User):
    def __init__(self, name, grade):
        print("Student.__init__ called.")
        super().__init__(name)
        self.grade = grade

    def log_in(self):
        print("Student.log_in() called.")
        super().log_in()
        self.in_class = True

oneil = Student("O'neil", 10)
oneil.log_in()
print(oneil.name, oneil.grade)