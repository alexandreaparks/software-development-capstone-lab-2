class Author:

    def __init__(self, name):
        self.name = name
        self.books = []  # create empty book title list

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
            print("This book is already in the list")  # print this error message
        else:  # else add the book to the books list
            self.books.append(book_title)


# main function used to create new author objects
def main():
    shakespeare = Author("William Shakespeare")  # create new author object
    shakespeare.publish("Hamlet")
    shakespeare.publish("Richard III")
    shakespeare.publish("Hamlet")  # try adding a duplicate book title - doesn't work

    print(shakespeare)  # uses __str__ method to print info about author object

    alexandrea = Author("Alexandrea")  # add another author
    print(alexandrea)  # alexandrea hasn't published any books so "No books" is printed


if __name__ == "__main__":
    main()  # call main function to start program
