#When starting the app, users are provided with a menu
# to choose whether they want to list, add, edit or share a book
#When the user starts the app next time, the stored books should be preserved (via csv)

def AddBook():
# The app inquires the user to provide the author and title of the book
# this book is saved in DB
    book_name =input("Insert a book name: ")
    author_name =input("Insert the author of the book : ")
    import csv
    with open("booksDB.csv", mode="w") as file:
        writer = csv.DictWriter(file,fieldnames=[
            "BookName", "AuthorName","SharedWith", "IsRead"
        ])
        writer.writerow({"BookName": book_name,
                     "AuthorName": author_name})
    print("Book was added successfully")

def ListBook():
    print("List a book option")

def UpdateBook():
    print("Update a book option")

def ShareBook():
    print("Share a book option")

#Step 1: Main menu
print("""
    Welcome reader to Cristian's Cojocea app for your favorite books to keep
       
                    The main menu commands are:
       
                1 represents 'Add a book' feature
                2 represents 'List of books' feature
                3 represents 'Update a book' feature
                4 represents 'Share your review for a book'
""")
option = int(input("Please choose an option -> "))

if option==1:
    AddBook()
elif option==2:
    ListBook()
elif option==3:
    UpdateBook()
elif option==4:
    ShareBook()
else:
    print("Your input is not a valid option, please try again")


