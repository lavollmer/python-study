# inheritance multiple classes relate to each other
# inheritance is a key feature

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("missing name")
        self.name = name


# class name(class name) = inherit all the classes attributes
class Student(Wizard):
    def __init__(self, name, house):
        # accessing Super(parent class i.e. Wizard), init method
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Dark Arts")
