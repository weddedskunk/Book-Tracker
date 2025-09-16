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
        print(f"{idx}. {book['title']} by book{['author']} [{book['status']}]")
    print("*" * 50)

#add new book to list
def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    status = input("Enter status (reading/completed/to read): ").strip().lower()

    if status not in ["reading", "completed", "to read"]:
        print("Invalid status")
    
    books.append({"Title": title, "author": author, "status": status})
    save_books(books)
    print(f"Book '{title}' added successfuly!\n")

#update the status of a book
def update_status(books):
    display_books(books) #considering dropping this part
    if not books: 
        return
    try:
        choice = int(input("Enter a book to update: "))
        if 1 <= choice <= len(books):
            new_status = input("Enter new status (reading/completed/to read): ")
            if new_status in ["reading", "completed", "to read"]:
                books[choice - 1]["status"] = new_status
                save_books(books)
                print("Book status updated!\n")
            else:
                print("Invalid status\n")
        else: 
            print("Invalid book number\n")
    except ValueError:
        print("Please enter a valid number\n")
