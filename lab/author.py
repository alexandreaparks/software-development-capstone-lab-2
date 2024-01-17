"""
Alexandrea Parks
author.py
1/17/2024
This program creates an Author class with instance variables for the name of an author and their published books
stored in a list. The class is used to create some Author objects.
"""


class Author:

    def __init__(self, name):
        self.name = name
        self.books = []

    # __str__ method is used to format/print data about an author object
    def __str__(self):
        # if self.books:
        #     book_list = ", ".join(self.books)
        # else:
        #     book_list = "No books"

        # shortcut for above code
        # if author has published books, the code on left of or runs
        # else if author doesn't have any published books, code on right runs
        book_list = ", ".join(self.books) or "No books"
        return f"Author's Name: {self.name}, Books Published: {book_list}"

    # publish method is used to add a book to books list
    def publish(self, book_title):
        if book_title in self.books:  # if book was already added to books list
            print("This book is already in the list")
        else:  # else add the book to the books list
            self.books.append(book_title)

        # can also use set - compare sizes of set


# main function used to create new author objects
def main():
    shakespeare = Author("William Shakespeare")  # create new author object
    shakespeare.publish("Hamlet")
    shakespeare.publish("Richard III")
    shakespeare.publish("Hamlet")  # try adding a duplicate book title - doesn't work
    print(shakespeare)  # uses __str__ method to print info about author object

    alexandrea = Author("Alexandrea")  # add another author
    print(alexandrea)  # alexandrea hasn't published any books so "No books" is printed

    partanen = Author("Anu Partanen")
    partanen.publish("The Nordic Theory of Everything")
    print(partanen)

    patterson = Author("James Patterson")
    patterson.publish("Along Came a Spider")
    patterson.publish("Roses Are Red")
    patterson.publish("The Girl in the Castle")
    print(patterson)



if __name__ == "__main__":
    main()
