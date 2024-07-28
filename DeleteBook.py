from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password="Mufaddal1234", database="lbs")
cur = con.cursor()

issueTable = "books_issued"
bookTable = "books"  # Book Table

def on_enter(event, widget):
    widget.config(bg='#001D4A', fg='white')

def on_leave(event, widget):
    widget.config(bg='#d1ccc0', fg='black')

def on_enter_quit(event, widget):
    widget.config(bg='#001D4A', fg='white')

def on_leave_quit(event, widget):
    widget.config(bg='#f7f1e3', fg='black')

def deleteBook():
    bid = bookInfo1.get()

    deleteSql = "delete from " + bookTable + " where bid = '" + bid + "'"
    deleteIssue = "delete from " + issueTable + " where bid = '" + bid + "'"

    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()

        messagebox.showinfo('Success', "Book Record Deleted Successfully")

    except:
        messagebox.showinfo("Please check Book ID")

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()

def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#F6AE2D")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#006992", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='#001D4A', fg='#EAF8BF', font=('Courier', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='#2F4858')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('Courier', 12))
    lb2.place(relx=0.05, rely=0.5, relheight=0.08)

    bookInfo1 = Entry(labelFrame, font=('Courier', 12))
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', font=('Courier', 12), command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    SubmitBtn.bind("<Enter>", lambda event: on_enter(event, SubmitBtn))
    SubmitBtn.bind("<Leave>", lambda event: on_leave(event, SubmitBtn))

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', font=('Courier', 12), command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    quitBtn.bind("<Enter>", lambda event: on_enter_quit(event, quitBtn))
    quitBtn.bind("<Leave>", lambda event: on_leave_quit(event, quitBtn))

    root.mainloop()
