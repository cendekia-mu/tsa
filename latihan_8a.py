class Person:
    _name = ""
    _age = 0
    _sex = ""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        # return f"Person(name={self.name}, age={self.age})"
        return f"{self._name}, {self._age}"

    def greet(self):
        return f"Hello, my name is {self._name} and I am {self._age} years old."

class Student(Person):
    _student_id = ""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id

    def __str__(self):
        return f"Student(name={self._name}, age={self._age}, student_id={self._student_id})"

    def study(self):
        return f"{self._name} is studying."
    
class Teacher(Person):
    _subject = ""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self._subject = subject

    def __str__(self):
        return f"Teacher(name={self._name}, age={self._age}, subject={self._subject})"

    def teach(self):
        return f"{self._name} is teaching {self._subject}."
    

p1 = Person("Alice", 30)
print(p1)
p1.name = "Satrio"
print(p1)
print(''.ljust(50, '-'))
s1 = Student("Bob", 20, "S12345")
print(s1)
print(s1.study())
print(''.ljust(50, '-'))

t1 = Teacher("Charlie", 40, "Math")
print(t1)
print(t1.teach())
# p1.age = 30
# print(p1.name, p1.age)
# print(p1)
# print(p1.greet())
