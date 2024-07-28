from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password="Mufaddal1234", database="lbs")
cur = con.cursor()

# Enter Table Names here
bookTable = "books"

def on_enter(event, widget):
    widget.config(bg='#001D4A', fg='white')

def on_leave(event, widget):
    widget.config(bg='#d1ccc0', fg='black')

def on_enter_quit(event, widget):
    widget.config(bg='#001D4A', fg='white')

def on_leave_quit(event, widget):
    widget.config(bg='#f7f1e3', fg='black')

def View(): 
    root = Tk()
    root.title("Library")
    root.geometry("600x500")  # Maintain the popup interface size

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#F6AE2D")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#006992", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books",bg='#001D4A', fg='#EAF8BF', font=('Courier', 18, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)  # Adjusted position and size for better view

    # Headers for the columns
    Label(labelFrame, text="%-10s%-20s%-20s%-10s" % ('BID', 'Title', 'Author', 'Qty'),
          bg='black', fg='white', font=('Courier', 10)).place(relx=0.07, rely=0.1)

    # Separator line
    Label(labelFrame, text="-"*70,
          bg='black', fg='white', font=('Courier', 10)).place(relx=0.05, rely=0.2)

    # Query to fetch books data including quantity
    getBooks = f"SELECT bid, title, author, quantity FROM {bookTable}"

    try:
        cur.execute(getBooks)
        con.commit()

        y = 0.3
        for i in cur:
            # Displaying each book's information
            Label(labelFrame, text="%-10s%-20s%-20s%-10s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white', font=('Courier', 10)).place(relx=0.07, rely=y)
            y += 0.1
    except Exception as e:
        messagebox.showinfo("Failed to fetch files from database", f"Error: {e}")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', font=('Courier', 12), command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    quitBtn.bind("<Enter>", lambda event: on_enter_quit(event, quitBtn))
    quitBtn.bind("<Leave>", lambda event: on_leave_quit(event, quitBtn))

    root.mainloop()


