class Author:

    def __init__(self, name):
        self.name = name
        self.books = []  # create empty book title list

    def __str__(self):
        # if self.books:
        #     book_list = ", ".join(self.books)
        # else:
        #     book_list = "No books"
        
        book_list = ", ".join(self.books) or "No books"  # shortcut
        return f"Author's Name: {self.name}, Books Published: {book_list}"

    def publish(self, book_title):

        self.books.append(book_title)


shakespeare = Author("William Shakespeare")
shakespeare.publish("Hamlet")
shakespeare.publish("Richard III")

print(shakespeare)

alexandrea = Author("Alexandrea")
print(alexandrea)