from dataclasses import dataclass

# use dataclass to remove boring code from programs
@dataclass
class Student:
    name: str  # instance variable in our student object
    school_id: str
    gpa: float

    # dataclass generates this method, but can still use it to override
    def __str__(self):  # for returning string representation of object
        return f"Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}"

def main():

    alexandrea = Student("Alexandrea", "yy2888bl", 4.0)  # create new student object
    print(alexandrea.name)
    print(alexandrea.school_id)
    print(alexandrea)

    sam = Student("Sam", "qwerty", 3.7)
    print(sam)


if __name__ == "__main__":
    main()
