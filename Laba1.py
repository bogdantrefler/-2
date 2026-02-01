class Humanity:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def info(self):
        return f"Ім'я: {self.name}, Вік: {self._age}"

    def activity(self):
        return "Людина живе"


class Student(Humanity):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def activity(self):
        return "Студент навчається"


person = Humanity("Іван", 40)
student = Student("Богдан", 18, "Університет")

print(person.info())
print(person.activity())

print(student.info())
print(student.activity())