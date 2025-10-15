from  latihan_8a import Person as Orang

# class Person:
#     _name = ""
#     _age = 0

class A(Orang):
    _sex = "L"


class B(Orang):
    _sex = "P"


class C(B,A):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"{self._name}, {self._age}, {self._sex}"

c = C("Diana", 25)
c._sex = "L"
print(c)
