from tkinter import *
from tkinter import messagebox
import pymysql

# Database connection details
mypass = "Mufaddal1234"  # Replace with your MySQL password
mydatabase = "lbs"  # Replace with your database name

# Establishing connection
con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()  # Cursor object to interact with MySQL database

# Function to display search result or message
def show_search_popup(message):
    messagebox.showinfo("Search Result", message)

# Function to perform search based on user input
def search_books(root):
    search_query = book_entry.get().strip()  # Trim leading and trailing whitespace

    # Clear any previous results
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Convert search query to lowercase for case-insensitive search
    search_query_lower = search_query.lower()

    # Fetch books from database related to the search query
    search_books_query = f"SELECT title, author, quantity FROM books WHERE LOWER(title) LIKE '%{search_query_lower}%' OR LOWER(author) LIKE '%{search_query_lower}%'"
    
    try:
        cur.execute(search_books_query)
        con.commit()
        books_found = cur.fetchall()

        if books_found:
            for index, book in enumerate(books_found):
                book_title = book[0]
                book_author = book[1]
                book_quantity = book[2]
                
                # Display only if quantity is 1 or more
                if book_quantity >= 1:
                    Label(result_frame, text=f"{index + 1}. {book_title} by {book_author}, Quantity: {book_quantity}", bg='white', font=('Arial', 12)).pack(pady=5)
                else:
                    Label(result_frame, text=f"{index + 1}. {book_title} by {book_author}, Quantity: Not Available", bg='white', font=('Arial', 12)).pack(pady=5)
            show_search_popup(f"{len(books_found)} books found matching your search criteria.")
        else:
            show_search_popup("No books found matching your search criteria.")
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching books: {e}")

# Create the tkinter window for the search functionality
def create_search_window():
    global root, book_entry, result_frame  # Define as global to use inside search_books

    root = Tk()
    root.title("Search Books")
    root.geometry("600x500")
    root.configure(bg='#F6AE2D')  # Set background color

    # Header Frame
    headingFrame1 = Frame(root, bg="#006992", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.12)
    headingLabel = Label(headingFrame1, text="Search Books", bg='#001D4A', fg='#EAF8BF', font=('Courier', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Input Frame
    input_frame = Frame(root, bg='white', bd=2)
    input_frame.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.1)
    book_entry = Entry(input_frame, font=('Arial', 14), bd=2)
    book_entry.insert(0, "Search your book...")
    book_entry.pack(side=LEFT, padx=10, pady=5, expand=True, fill='both')

    # Search Button
    def on_search_enter(e):
        search_button['background'] = '#27476E'
        search_button['foreground'] = 'white'

    def on_search_leave(e):
        search_button['background'] = 'grey'
        search_button['foreground'] = 'white'

    search_button = Button(root, text="Search", bg='grey', fg='white', font=('Arial', 12, 'bold'), command=lambda: search_books(root))
    search_button.place(relx=0.75, rely=0.25, relwidth=0.15, relheight=0.1)
    search_button.bind("<Enter>", on_search_enter)
    search_button.bind("<Leave>", on_search_leave)

    # Frame for displaying search results
    result_frame = Frame(root, bg='#2F4858', bd=2)
    result_frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)

    # Done Button
    def on_done_enter(e):
        done_button['background'] = '#27476E'
        done_button['foreground'] = 'white'

    def on_done_leave(e):
        done_button['background'] = 'grey'
        done_button['foreground'] = 'white'

    done_button = Button(root, text="Done", bg='grey', fg='white', font=('Arial', 12, 'bold'), command=root.destroy)
    done_button.place(relx=0.4, rely=0.92, relwidth=0.2, relheight=0.06)
    done_button.bind("<Enter>", on_done_enter)
    done_button.bind("<Leave>", on_done_leave)

    root.mainloop()  # Start the Tkinter event loop
