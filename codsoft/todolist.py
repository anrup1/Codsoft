import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("H4CK3R TO-DO L1ST")
        self.master.configure(bg="#0d0208")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(master, width=40, bg="#0d0208", fg="#00ff00", insertbackground="#00ff00", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<FocusIn>", self.highlight_border)
        self.task_entry.bind("<FocusOut>", self.reset_border)
        
        self.add_button = tk.Button(master, text="ADD TASK", command=self.add_task, bg="#00ff00", fg="#0d0208", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.add_button.pack()
        
        self.task_listbox = tk.Listbox(master, width=40, bg="#0d0208", fg="#00ff00", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.task_listbox.pack(pady=10)
        
        self.delete_button = tk.Button(master, text="DELETE TASK", command=self.delete_task, bg="#00ff00", fg="#0d0208", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.delete_button.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Pl3ase 3nter a t4sk!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")
    
    def highlight_border(self, event):
        self.task_entry.config(bd=2, relief=tk.SOLID)

    def reset_border(self, event):
        self.task_entry.config(bd=2, relief=tk.FLAT)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
