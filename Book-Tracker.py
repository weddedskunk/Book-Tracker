import json
import os

Book_File = "books.json"

#Load books from file or return file not found error
def load_books():
    if os.path.exists(Book_File):
        with open(Book_File, "r") as f:
            return json.load(f)
    else:
        print("File not found!")
        return

#saves books to json file
def save_books(books):
    with open(Book_File, "w") as f:
        json.dump(books, f, indent=4)

#display books in a formatted table
def display_books(books):
    if not books:
        print("No books found")
        return
    print("\nYour Book list: ")
    print("*" * 50)
    for idx, book in enumerate(books, 1):
        print(f{idx}. {book['title']} by book{['author']} [{book['status']}])
    print("*" * 50)

#add new book to list