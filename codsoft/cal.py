import tkinter as tk
from tkinter import messagebox

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
        else:
            result = num1 / num2

    messagebox.showinfo("Result", f"The result is: {result}")

# Create the main window
window = tk.Tk()
window.title("HACK CALCULATOR")
window.geometry("400x200")
window.configure(bg="#000000")

# Create labels
label_num1 = tk.Label(window, text="ENTER FIRST NUMBER:", font=("Courier", 12), fg="#00FF00", bg="#000000")
label_num1.grid(row=0, column=0, padx=5, pady=5)
label_num2 = tk.Label(window, text="ENTER SECOND NUMBER:", font=("Courier", 12), fg="#00FF00", bg="#000000")
label_num2.grid(row=1, column=0, padx=5, pady=5)
label_operation = tk.Label(window, text="CHOOSE OPERATION:", font=("Courier", 12), fg="#00FF00", bg="#000000")
label_operation.grid(row=2, column=0, padx=5, pady=5)

# Create entry widgets
entry_num1 = tk.Entry(window, bg="#333333", fg="#00FF00", insertbackground="#00FF00", font=("Courier", 12))
entry_num1.grid(row=0, column=1, padx=5, pady=5)
entry_num2 = tk.Entry(window, bg="#333333", fg="#00FF00", insertbackground="#00FF00", font=("Courier", 12))
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Create operation dropdown
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar(window)
operation_var.set(operations[0])  # Default value
operation_dropdown = tk.OptionMenu(window, operation_var, *operations)
operation_dropdown.config(bg="#333333", fg="#00FF00", font=("Courier", 12))
operation_dropdown.grid(row=2, column=1, padx=5, pady=5)

# Create calculate button
calculate_button = tk.Button(window, text="HACK", command=calculate, bg="#00FF00", fg="#000000", font=("Courier", 14))
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop
window.mainloop()
