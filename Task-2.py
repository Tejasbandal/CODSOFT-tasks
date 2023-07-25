import tkinter as tk
from tkinter import ttk

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Function to evaluate the expression
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        output.configure(text=str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        output.configure(text="")

# Function to clear the input and output
def clear_all():
    entry.delete(0, tk.END)
    output.configure(text="")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Configure color scheme
s = ttk.Style()
s.configure("TButton",
            font=("Helvetica", 14),
            padding=10,
            width=5)

# Create the entry widget
entry = ttk.Entry(window, font=("Helvetica", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Create the output label
output = ttk.Label(window, text="", font=("Helvetica", 14))
output.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Create buttons
buttons = [
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("/", 2, 3),
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("*", 3, 3),
    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("-", 4, 3),
    ("0", 5, 0),
    (".", 5, 1),
    ("+", 5, 2),
]

# Create and place the buttons
for button in buttons:
    text, row, column = button
    button = ttk.Button(window, text=text, command=lambda text=text: button_click(text))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="ew")

# Create the equals button
equals_button = ttk.Button(window, text="=", command=calculate)
equals_button.grid(row=5, column=3, padx=5, pady=5, sticky="ew")

# Create the clear all button
clear_button = ttk.Button(window, text="C", command=clear_all)
clear_button.grid(row=5, column=2, padx=5, pady=5, sticky="ew")

# Create the addition button
addition_button = ttk.Button(window, text="+", command=lambda: button_click("+"))
addition_button.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

# Run the application
window.mainloop()
