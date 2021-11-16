class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'student: {self.name}'

    def is_passed(self) -> bool:
        if self.marks > 50:
            return bool(1)
        else:
            return bool(0)
