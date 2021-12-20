class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get(self):
        print('Name '+self.name + " Id "+str(self.id))

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def __gt__(self, other):
        return self.id > other.id

    def __add__(self, other):
        return self.id + other.id


s1 = Student("MD Pabel", 11711111111)
s2 = Student("MD Pabel", 11711111111)

print(s1 == s2)
print(s1 > s2)
print(s1 + s2)

s1.get()
