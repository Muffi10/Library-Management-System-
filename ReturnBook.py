from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase = "lbs"

con = pymysql.connect(host="localhost", user="root", password="Mufaddal1234", database="lbs")
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books"
allBid = []  # To store all the Book IDs

def returnn():
    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status

    bid = bookInfo1.get()

    extractBid = "select bid from " + issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])
        
        if bid in allBid:
            checkAvail = "select quantity from " + bookTable + " where bid = '" + bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                current_quantity = i[0]
                
            status = True

        else:
            messagebox.showinfo("Error", "Book ID not present in issued records")
            return
    except Exception as e:
        messagebox.showinfo("Error", f"Can't fetch Book IDs\nError: {e}")
        return
    
    issueSql = "delete from " + issueTable + " where bid = '" + bid + "'"
    updateQuantity = "update " + bookTable + " set quantity = quantity + 1 where bid = '" + bid + "'"
    
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateQuantity)
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            messagebox.showinfo('Message', "Please check the book ID")
            return
    except Exception as e:
        messagebox.showinfo("Search Error", f"The value entered is wrong, Try again\nError: {e}")
    
    allBid.clear()
    root.destroy()

def returnBook(): 
    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#F6AE2D")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#006992", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg='#001D4A', fg='#EAF8BF', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='#2F4858')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)   

    # Book ID to Delete
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('Arial', 12))
    lb1.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame, font=('Arial', 12))
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="Return", bg='#d1ccc0', fg='black', font=('Arial', 12), command=returnn)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    SubmitBtn.bind("<Enter>", lambda e: SubmitBtn.config(bg='#001D4A'))
    SubmitBtn.bind("<Leave>", lambda e: SubmitBtn.config(bg='#d1ccc0'))

    # Quit Button
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', font=('Arial', 12), command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    quitBtn.bind("<Enter>", lambda e: quitBtn.config(bg='#001D4A'))
    quitBtn.bind("<Leave>", lambda e: quitBtn.config(bg='#f7f1e3'))

    root.mainloop()


