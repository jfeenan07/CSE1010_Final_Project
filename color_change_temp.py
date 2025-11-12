import os
import random
import tkinter as tk

def commence_budget():
    pass
root = tk.Tk()
root.title("BudgetBuddy")

colors = ["#FF0000", "#FFE600", "#15FF00", "#0019FF", "#BB00FF", "#FF00BF"]
selected_color = random.choice(colors)
root.configure(bg=selected_color)

label = tk.Label(
    root,
    text="Welcome to BudgetBuddy, your personal Budgeting Assistant!",
    bg=selected_color,
    font=("Papyrus", 20)
)
label.pack(padx=60, pady=60)

button = tk.Button(root, text="Commence Budgeting", command = commence_budget)

root.mainloop()
