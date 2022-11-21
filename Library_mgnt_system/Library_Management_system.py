"""
Create a library class
display book
lend book - (who owns the book if not present)
add book
return book

HarryLibrary = Library(listofbooks, library_name)


dictionary(books-nameofperson)

create a main function and run an infinite while loop asking
users for their input
"""

import file_manager


class Library:
    file_manager.readFile()
    bookRecord = file_manager.bookRecord

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name

    def viewBooks(self):
        print("Books in library are:->")
        for index, book in enumerate(self.list_of_books):
            print(f"\t{index+1}.{book}")

    def lendBooks(self, bookName, personName):
        for book in self.list_of_books:
            if book.upper() == bookName.upper():
                if (self.bookRecord[book] == "None"):
                    self.bookRecord[book] = personName
                    file_manager.bookRecord[book] = personName
                    file_manager.bookList_changer()
                    print(f"{book} was successfully lended to {personName}")
                    break
                else:
                    print(
                        f"{self.bookRecord[book]} has already lended the book.")
                    break
            else:
                return "Book unavailable."

    def addBooks(self, bookName):
        (self.list_of_books).append(bookName)  # updating list of books
        self.bookRecord[bookName.capitalize()] = "None"  # updating dictionary
        file_manager.bookRecord[bookName.capitalize()] = "None"
        file_manager.writeFile(bookName, "None")

    def returnBook(self, bookName, personName):
        for book in self.list_of_books:
            if book.upper() == bookName.upper():
                if(self.bookRecord[bookName.capitalize()] == personName):
                    self.bookRecord[bookName.capitalize()] = "None"
                    file_manager.bookRecord[book] = "None"
                    file_manager.bookList_changer()
                    print("Successfully returned book.")
                else:
                    print("You haven't lended this book.")
            else:
                return "This book is not available in library."

    def free_books(self):
        for key, value in self.bookRecord.items():
            if self.bookRecord[key] == "None":
                print(f"\t{key}")


kiranLibrary = Library(file_manager.book_list(), "Kiran's Library")

print("\n\t\t\t\tONLINE LIBRARY\n")

print("What's your name dude?")
personName = input("\t----> ")
while True:
    if __name__ == "__main__":

        print("\nWhat are you willing to do?\n"
              "\t1.View Books in Library\n"
              "\t2.Lend Book\n"
              "\t3.Return Book\n"
              "\t4.View free books\n"
              "\t5.Donate Book")

        usr_inp = int(input("(Enter the choice in number)----> "))
        if (usr_inp == 1):
            kiranLibrary.viewBooks()

        elif (usr_inp == 2):
            print("Which book do you want to lend?")
            bookName = input("\t----> ")
            print(kiranLibrary.lendBooks(bookName, personName))

        elif (usr_inp == 3):
            print("Which book do you want to return?")
            bookName = input("---->")
            kiranLibrary.returnBook(bookName, personName)

        elif(usr_inp == 4):
            kiranLibrary.free_books()

        elif (usr_inp == 5):
            print("Which book do you want to donate?")
            bookName = input("---->")
            kiranLibrary.addBooks(bookName)
