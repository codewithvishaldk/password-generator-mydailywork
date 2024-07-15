import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, include_numbers, include_uppercase, include_special):
    characters = string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_button_click():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the length.")
        return

    include_numbers = numbers_var.get()
    include_uppercase = uppercase_var.get()
    include_special = special_var.get()

    password = generate_password(length, include_numbers, include_uppercase, include_special)
    result_label.config(text=f"Generated Password: {password}")

# Set up the main application window
app = tk.Tk()
app.title("Password Generator")

# Length input
tk.Label(app, text="Enter the desired length of the password:").pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)

# Options for including numbers, uppercase letters, and special characters
numbers_var = tk.BooleanVar()
tk.Checkbutton(app, text="Include Numbers", variable=numbers_var).pack(pady=5)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(app, text="Include Uppercase Letters", variable=uppercase_var).pack(pady=5)

special_var = tk.BooleanVar()
tk.Checkbutton(app, text="Include Special Characters", variable=special_var).pack(pady=5)

# Generate button
generate_button = tk.Button(app, text="Generate Password", command=on_generate_button_click)
generate_button.pack(pady=10)

# Result label
result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Run the application
app.mainloop()
