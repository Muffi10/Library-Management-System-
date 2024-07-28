from tkinter import *
from PIL import ImageTk, Image
import pymysql
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from searchBook import create_search_window  # Import the function to create local search window
from apii import create_search_interface  # Import the function to create online search interface

mypass = "root"  # use your own password
mydatabase = "db"  # The database name

con = pymysql.connect(host="localhost", user="root", password='Mufaddal1234', database='lbs')
cur = con.cursor()  # cur -> cursor

def main_interface():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    same = True
    n = 1

    # Adding a background image
    background_image = Image.open("lib1.png")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth * n)
    if same:
        newImageSizeHeight = int(imageSizeHeight * n)
    else:
        newImageSizeHeight = int(imageSizeHeight / n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.LANCZOS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(root)
    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#006992", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame1, text="BNMIT LIBRARY", bg='#001D4A', fg='#EAF8BF', font=('Courier', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    def on_enter(e):
        e.widget['background'] = '#27476E'
        e.widget['foreground'] = 'white'


    def on_leave(e):
        e.widget['background'] = '#EAF8BF'
        e.widget['foreground'] = '#001D4A'


    button_font = ('Times New Roman', 12, 'bold')

    # Adjust button height and margin
    button_height = 0.08
    button_margin = 0.02

    btn1 = Button(root, text="Add Book Details", bg='#EAF8BF', fg='#001D4A', command=addBook, font=button_font, padx=10, pady=5)
    btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=button_height)
    btn1.bind("<Enter>", on_enter)
    btn1.bind("<Leave>", on_leave)

    btn2 = Button(root, text="Delete Book", bg='#EAF8BF', fg='#001D4A', command=delete, font=button_font, padx=10, pady=5)
    btn2.place(relx=0.28, rely=0.3 + button_height + button_margin, relwidth=0.45, relheight=button_height)
    btn2.bind("<Enter>", on_enter)
    btn2.bind("<Leave>", on_leave)

    btn3 = Button(root, text="View Book List", bg='#EAF8BF', fg='#001D4A', command=View, font=button_font, padx=10, pady=5)
    btn3.place(relx=0.28, rely=0.3 + 2 * (button_height + button_margin), relwidth=0.45, relheight=button_height)
    btn3.bind("<Enter>", on_enter)
    btn3.bind("<Leave>", on_leave)

    btn4 = Button(root, text="Issue Book to Student", bg='#EAF8BF', fg='#001D4A', command=issueBook, font=button_font, padx=10, pady=5)
    btn4.place(relx=0.28, rely=0.3 + 3 * (button_height + button_margin), relwidth=0.45, relheight=button_height)
    btn4.bind("<Enter>", on_enter)
    btn4.bind("<Leave>", on_leave)

    btn5 = Button(root, text="Return Book", bg='#EAF8BF', fg='#001D4A', command=returnBook, font=button_font, padx=10, pady=5)
    btn5.place(relx=0.28, rely=0.3 + 4 * (button_height + button_margin), relwidth=0.45, relheight=button_height)
    btn5.bind("<Enter>", on_enter)
    btn5.bind("<Leave>", on_leave)

    # Button for Local Book Search
    btn_search = Button(root, text="Search Book", bg='#EAF8BF', fg='#001D4A', command=create_search_window, font=button_font, padx=10, pady=5)
    btn_search.place(relx=0.28, rely=0.3 + 5 * (button_height + button_margin), relwidth=0.45, relheight=button_height)
    btn_search.bind("<Enter>", on_enter)
    btn_search.bind("<Leave>", on_leave)

    # Button for Online Book Search
    btn_search_online = Button(root, text="Search Online", bg='#EAF8BF', fg='#001D4A', command=create_search_interface, font=button_font, padx=10, pady=5)
    btn_search_online.place(relx=0.28, rely=0.3 + 6 * (button_height + button_margin), relwidth=0.45, relheight=button_height)
    btn_search_online.bind("<Enter>", on_enter)
    btn_search_online.bind("<Leave>", on_leave)

    root.mainloop()

if __name__ == "__main__":
    import admin
