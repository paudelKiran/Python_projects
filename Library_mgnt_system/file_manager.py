bookRecord = {}


def readFile():
    with open("bookLists.txt", "r") as file:
        for items in file.readlines():
            if items[-1:] == "\n":
                book = items[0:(len(items)-1)]
                bookRecord[book.split(":")[0]] = book.split(":")[1]
            else:
                book = items
                bookRecord[book.split(":")[0]] = book.split(":")[1]


def writeFile(bookName, personName):
    with open("bookLists.txt", "a") as file:
        file.write(f"{bookName}:{personName}\n")


def book_list():
    readFile()
    list_of_books = (list(bookRecord.keys()))
    return list_of_books


def bookList_changer():
    # removing every content from file
    with open("bookLists.txt", "w") as f:
        f.truncate(0)
    # writing updated content again
    with open("bookLists.txt", "a") as file:
        for key, values in bookRecord.items():
            file.writelines(f"{key}:{values}\n")
