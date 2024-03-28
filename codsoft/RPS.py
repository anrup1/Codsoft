import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("H4CK3R R0CK-P4P3R-SC1SS0RS G4M3")
        self.master.configure(bg="#0d0208")
        
        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_choice = tk.StringVar(master)
        self.user_choice.set(self.choices[0])  # Default choice
        
        self.choice_label = tk.Label(master, text="Choose your weapon:", bg="#0d0208", fg="#00ff00", font=("Courier", 12))
        self.choice_label.pack(pady=10)
        
        self.choice_menu = tk.OptionMenu(master, self.user_choice, *self.choices)
        self.choice_menu.config(bg="#0d0208", fg="#00ff00", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.choice_menu.pack()
        
        self.play_button = tk.Button(master, text="PLAY", command=self.play_game, bg="#00ff00", fg="#0d0208", bd=2, relief=tk.FLAT, font=("Courier", 12))
        self.play_button.pack(pady=10)
        
    def play_game(self):
        user_choice = self.user_choice.get()
        computer_choice = random.choice(self.choices)
        
        result = self.determine_winner(user_choice, computer_choice)
        
        messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")
        
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.user_choice.set(self.choices[0])  # Reset choice to default
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "You win!"
        else:
            return "You lose!"

def main():
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
