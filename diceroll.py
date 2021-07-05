import tkinter as tk
import random

root = tk.Tk()
root.title("Dice Roll")
# The 0 here is the default value
def dice(num2=0):
    if num2 < 10:

        num=["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

        roll=str(random.choice(num))
        dice_label.config(text=roll)

        # After 500ms call `dice` again but with `num2+1` as it's argument
        root.after(300, dice, num2+1)
    



welcome_label = tk.Label(root, text="Welcome to Dice Roll")
welcome_label.grid(row=0, column=0)

dice_label = tk.Label(root, font=("Helvitica", 300, "bold"), text="")
dice_label.grid(row=1, column=0)

button = tk.Button(root,text="Click to Roll", command=dice)
button.grid(row=2,column=0,padx = 175)

root.mainloop()