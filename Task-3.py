import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    length = int(length_entry.get())
    if length > 0:
        password = generate_password(length)
        messagebox.showinfo("Generated Password", f"Password: {password}")
    else:
        messagebox.showerror("Error", "Please enter a valid password length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200")  # Set the size of the window to 300x200

# Configure a dark color scheme
window.config(bg="black")
length_label = tk.Label(window, text="Password Length:", bg="black", fg="white")
length_label.pack()
length_entry = tk.Entry(window, bg="black", fg="white")
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_button_clicked, bg="black", fg="white")
generate_button.pack()

window.mainloop()
