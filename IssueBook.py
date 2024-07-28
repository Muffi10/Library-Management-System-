from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password="Mufaddal1234", database="lbs")
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued"
bookTable = "books"

allBid = []  # To store all the Book IDs

def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractBid = "select bid from " + bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkQuantity = "select quantity from " + bookTable + " where bid = '" + bid + "'"
            cur.execute(checkQuantity)
            con.commit()
            for i in cur:
                quantity = i[0]

            if quantity > 0:
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Book ID not present")
            return
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "insert into " + issueTable + " (bid, issuedto) values ('" + bid + "','" + issueto + "')"
    updateQuantity = "update " + bookTable + " set quantity = quantity - 1 where bid = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateQuantity)
            con.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message', "No more copies of this book available")
            root.destroy()
            return
    except Exception as e:
        messagebox.showinfo("Search Error", f"The value entered is wrong, Try again\nError: {e}")

    allBid.clear()

def on_enter(event, widget):
    widget.config(bg='#001D4A', fg='white')

def on_leave(event, widget):
    widget.config(bg='#d1ccc0', fg='black')

def issueBook():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#F6AE2D")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#006992", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='#001D4A', fg='#EAF8BF', font=('Courier', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='#2F4858')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('Courier', 12))
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame, font=('Courier', 12))
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white', font=('Courier', 12))
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame, font=('Courier', 12))
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', font=('Courier', 14), command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    issueBtn.bind("<Enter>", lambda event: on_enter(event, issueBtn))
    issueBtn.bind("<Leave>", lambda event: on_leave(event, issueBtn))

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', font=('Courier', 14), command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    quitBtn.bind("<Enter>", lambda event: on_enter(event, quitBtn))
    quitBtn.bind("<Leave>", lambda event: on_leave(event, quitBtn))

    root.mainloop()
