import tkinter as tk
from tkinter import scrolledtext
import requests

def on_enter(event, widget):
    widget.config(bg='#27476E', fg='white')

def on_leave(event, widget):
    widget.config(bg='white', fg='black')

def create_search_interface():
    def search_books():
        keyword = entry.get().strip()
        if not keyword:
            result_box.delete('1.0', tk.END)
            result_box.insert(tk.END, "Please enter a keyword to search.")
            return
        
        url = f'https://www.googleapis.com/books/v1/volumes?q={keyword}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            
            if items:
                result_box.delete('1.0', tk.END)
                for item in items:
                    volume_info = item.get('volumeInfo', {})
                    title = volume_info.get('title', 'Unknown Title')
                    authors = volume_info.get('authors', ['Unknown Author'])
                    result_box.insert(tk.END, f"Title: {title}\n")
                    result_box.insert(tk.END, f"Authors: {', '.join(authors)}\n\n")
            else:
                result_box.delete('1.0', tk.END)
                result_box.insert(tk.END, "No book results found.")
        else:
            result_box.delete('1.0', tk.END)
            result_box.insert(tk.END, f"Error: {response.status_code}")

    # Create the main window for online book search
    search_window = tk.Tk()
    search_window.title("Search Books Online")
    search_window.geometry("600x500")

    # Styling
    search_window.configure(bg='#F6AE2D')

    # Header
    header = tk.Label(search_window, text="Search Books Online", font=('Courier', 18, 'bold'), bg='#006992', fg='#EAF8BF', bd=5)
    header.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    # Input Frame
    input_frame = tk.Frame(search_window, bg='#2F4858', bd=5)
    input_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)

    entry = tk.Entry(input_frame, width=40, font=('Arial', 12))  # Reduced width
    entry.pack(side=tk.LEFT, padx=10, pady=5)

    search_button = tk.Button(input_frame, text="Search", font=('Arial', 12, 'bold'), command=search_books)
    search_button.pack(side=tk.LEFT, padx=10)
    search_button.bind("<Enter>", lambda event: on_enter(event, search_button))
    search_button.bind("<Leave>", lambda event: on_leave(event, search_button))

    # Result Box
    result_box = scrolledtext.ScrolledText(search_window, width=80, height=15, wrap=tk.WORD, font=('Arial', 12))
    result_box.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)

    search_window.mainloop()
