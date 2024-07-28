from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    quantity = bookInfo4.get()

    if not quantity.isdigit():
        messagebox.showinfo("Error", "Quantity must be an integer")
        return

    insertBooks = f"INSERT INTO {bookTable} (bid, title, author, quantity) VALUES ('{bid}', '{title}', '{author}', {quantity})"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except Exception as e:
        messagebox.showinfo("Error", f"Can't add data into Database\n{e}")

    root.destroy()

def on_enter(event, widget):
    widget.config(bg='#001D4A', fg='white')

def on_leave(event, widget):
    widget.config(bg='#d1ccc0', fg='black')

def addBook(): 
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass = "root"
    mydatabase = "lbs"

    con = pymysql.connect(host="localhost", user="root", password="Mufaddal1234", database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"  # Book Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#F6AE2D")
    Canvas1.pack(expand=True, fill=BOTH)
        
    headingFrame1 = Frame(root, bg="#006992", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Add Books", bg='#001D4A', fg='#EAF8BF', font=('Courier', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='#2F4858')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
        
    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('Courier', 12))
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame, font=('Courier', 12))
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white', font=('Courier', 12))
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame, font=('Courier', 12))
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white', font=('Courier', 12))
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame, font=('Courier', 12))
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Number of Books
    lb4 = Label(labelFrame, text="Quantity : ", bg='black', fg='white', font=('Courier', 12))
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame, font=('Courier', 12))
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)
        
    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', font=('Courier', 14), command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    SubmitBtn.bind("<Enter>", lambda event: on_enter(event, SubmitBtn))
    SubmitBtn.bind("<Leave>", lambda event: on_leave(event, SubmitBtn))
    
    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', font=('Courier', 14), command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    quitBtn.bind("<Enter>", lambda event: on_enter(event, quitBtn))
    quitBtn.bind("<Leave>", lambda event: on_leave(event, quitBtn))
    
    root.mainloop()
