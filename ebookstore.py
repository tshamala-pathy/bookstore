import sqlite3


# Create a connection to the database (or create a new one if it doesn't exist)
conn = sqlite3.connect("bookstore.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store book information
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    quantity INTEGER
)
""")

# Commit the changes and close the connection
conn.commit()
conn.close()

# Function to add a new book to the database
def add_book(title, author, quantity):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)", (title, author, quantity))
    conn.commit()
    conn.close()

# Function to update book information
def update_book(book_id, title, author, quantity):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, quantity=? WHERE id=?", (title, author, quantity, book_id))
    conn.commit()
    conn.close()

# Function to delete a book from the database
def delete_book(book_id):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

# Function to search for a specific book by title or author
def search_books(query):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + query + '%', '%' + query + '%'))
    books = cursor.fetchall()
    conn.close()
    return books


# Function to display the main menu
def main_menu():
    while True:
        print("\nBookstore Management Menu:")
        print("1. Enter a new book")
        print("2. Update book information")
        print("3. Delete a book")
        print("4. Search for books")
        print("0. Exit")
        
        choice = input("Please enter your choice: ")
        
        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            quantity = int(input("Enter the quantity: "))
            
            add_book(title, author, quantity)
            print("book added succssefuly!")
            
        elif choice == "2":
            book_id = int(input("Enter the book ID to update: "))
            title = input("Enter the new title: ")
            author = input("Enter the new author: ")
            quantity = int(input("Enter the new quantity: "))
            
            update_book(book_id, title, author, quantity)
            print("book informations update successfuly!")
            
        elif choice == "3":
            book_id = int(input("Enter the book ID to delete: "))
            delete_book(book_id)
            print("book deleted.")
            
        elif choice == "4":
            query = input("Enter the title or author to search for: ")
            result = search_books(query)
            if result:
                for book in result:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
            else:
                print("No matching books found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
