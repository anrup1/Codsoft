import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("H4CK3R P4SSW0RD G3N3R4T0R")
        self.master.configure(bg="#0d0208")
        
        self.length_label = tk.Label(master, text="Enter password length:", bg="#0d0208", fg="#00ff00", font=("Courier", 12))
        self.length_label.pack(pady=10)
        
        self.length_entry = tk.Entry(master, bg="#0d0208", fg="#00ff00", insertbackground="#00ff00", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.length_entry.pack()
        
        self.generate_button = tk.Button(master, text="GENERATE PASSWORD", command=self.generate_password, bg="#00ff00", fg="#0d0208", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.generate_button.pack(pady=10)
        
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showwarning("Warning", "Password length must be a positive integer!")
                return
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
            messagebox.showinfo("Generated Password", password)
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid integer for password length!")

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
