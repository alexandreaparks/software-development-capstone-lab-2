from dataclasses import dataclass

# use dataclass to remove boring code from programs
@dataclass
class Student:
    # data class generates the __init__ method
    name: str  # don't need to use self.name and you specify the data type
    school_id: str
    gpa: float

    # dataclass generates this method, but can still use it to override
    def __str__(self):  # for returning string representation of object
        return f"Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}"

# main function used to create new student objects
def main():

    alexandrea = Student("Alexandrea", "yy2888bl", 4.0)  # create new student object
    print(alexandrea)  # this uses the __str__ method to format/print data about student

    sam = Student("Sam", "qwerty", 3.7)
    print(sam)

    bob = Student("Bob", "6296233", 3.5)
    print(bob)


if __name__ == "__main__":
    main()
