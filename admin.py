import tkinter as tk
from tkinter import messagebox
import pymysql

# Database connection
def connect_db():
    return pymysql.connect(host="localhost", user="root", password="Mufaddal1234", database="lbs")

# Function to handle admin signup
def signup():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    full_name = fullname_entry.get()
    phone = phone_entry.get()

    if not username or not password or not email or not full_name or not phone:
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        con = connect_db()
        cur = con.cursor()

        query = "INSERT INTO admin (username, password, email, full_name, phone) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (username, password, email, full_name, phone))
        con.commit()

        messagebox.showinfo("Success", "Signup successful")
        con.close()
        clear_signup_fields()
        show_login()
    except Exception as e:
        con.rollback()
        messagebox.showerror("Error", f"Failed to signup. Error: {e}")

# Function to handle admin login
def login(success_callback):
    username = login_username_entry.get()
    password = login_password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Username and password are required")
        return

    try:
        con = connect_db()
        cur = con.cursor()

        query = "SELECT * FROM admin WHERE username=%s AND password=%s"
        cur.execute(query, (username, password))
        result = cur.fetchone()

        if result:
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            root.destroy()
            success_callback()  # Call the success callback function to load the main interface
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

        con.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error connecting to database: {e}")

# Function to clear signup fields
def clear_signup_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    fullname_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Function to show signup frame
def show_signup():
    login_frame.pack_forget()
    signup_frame.pack(fill="both", expand=True)

# Function to show login frame
def show_login():
    signup_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

# Create the main window
root = tk.Tk()
root.title("Admin Login/Signup")
root.geometry("400x480")

# Login Frame
login_frame = tk.Frame(root)
login_frame.pack(fill="both", expand=True)

login_header = tk.Label(login_frame, text="Admin Login", font=('Courier', 18, 'bold'))
login_header.pack(pady=20)

login_username_label = tk.Label(login_frame, text="Username", font=('Courier', 12))
login_username_label.pack(pady=5)
login_username_entry = tk.Entry(login_frame, font=('Courier', 12))
login_username_entry.pack(pady=5)

login_password_label = tk.Label(login_frame, text="Password", font=('Courier', 12))
login_password_label.pack(pady=5)
login_password_entry = tk.Entry(login_frame, show='*', font=('Courier', 12))
login_password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", command=lambda: login(load_main_interface), font=('Courier', 12))
login_button.pack(pady=20)

signup_switch_button = tk.Button(login_frame, text="Sign Up", command=show_signup, font=('Courier', 12))
signup_switch_button.pack(pady=10)

# Signup Frame
signup_frame = tk.Frame(root)

signup_header = tk.Label(signup_frame, text="Admin Signup", font=('Courier', 18, 'bold'))
signup_header.pack(pady=20)

username_label = tk.Label(signup_frame, text="Username", font=('Courier', 12))
username_label.pack(pady=5)
username_entry = tk.Entry(signup_frame, font=('Courier', 12))
username_entry.pack(pady=5)

password_label = tk.Label(signup_frame, text="Password", font=('Courier', 12))
password_label.pack(pady=5)
password_entry = tk.Entry(signup_frame, show='*', font=('Courier', 12))
password_entry.pack(pady=5)

email_label = tk.Label(signup_frame, text="Email", font=('Courier', 12))
email_label.pack(pady=5)
email_entry = tk.Entry(signup_frame, font=('Courier', 12))
email_entry.pack(pady=5)

fullname_label = tk.Label(signup_frame, text="Full Name", font=('Courier', 12))
fullname_label.pack(pady=5)
fullname_entry = tk.Entry(signup_frame, font=('Courier', 12))
fullname_entry.pack(pady=5)

phone_label = tk.Label(signup_frame, text="Phone", font=('Courier', 12))
phone_label.pack(pady=5)
phone_entry = tk.Entry(signup_frame, font=('Courier', 12))
phone_entry.pack(pady=5)

signup_button = tk.Button(signup_frame, text="Sign Up", command=signup, font=('Courier', 12))
signup_button.pack(pady=20)

login_switch_button = tk.Button(signup_frame, text="Login", command=show_login, font=('Courier', 12))
login_switch_button.pack(pady=10)

def load_main_interface():
    import main
    main.main_interface()

root.mainloop()
