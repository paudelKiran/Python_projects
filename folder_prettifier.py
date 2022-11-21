
# Oh soldier Prettify my Folder

# path, dictionary file, format

# def soldier("C://", "harry.txt", "jpg")

def folder_prettifyer(path, filee, format):
    i = 1
    import os
    os.chdir(path)
    files = os.listdir(path)

    with open(filee) as f:
        list_file = f.read().split("\n")

    for file in files:
        if file not in list_file:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i += 1


folder_prettifyer(r"C:\Users\Kiran Paudel\Desktop\python",
                  r"C:\Users\Kiran Paudel\Desktop\python\subsidary.txt", ".jpg")
