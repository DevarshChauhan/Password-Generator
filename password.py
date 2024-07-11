import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Create label and entry for password length
        self.length_label = tk.Label(master, text="Enter password length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(master, width=10)
        self.length_entry.pack()

        # Create generate button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        # Create label to display generated password
        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.pack()
        self.password_display = tk.Label(master, text="", wraplength=200)
        self.password_display.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.password_display.config(text=password)

root = tk.Tk()
my_password_generator = PasswordGenerator(root)
root.mainloop()