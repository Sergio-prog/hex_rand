from tkinter import *
import random

rand = random.randint(0, 16777215)
r_hex = hex(rand).replace("0x", "")
r3_hex = "#" + r_hex

if (len(r_hex) - 1) < 6:
    r_hex = str("0" * (6 - len(r_hex))) + str(r_hex)
    r3_hex = "#" + r_hex

print(r3_hex, rand)

root = Tk()
root.title(r3_hex)
root.geometry("200x150")
root.config(bg=(str(r3_hex)))

hex_var = StringVar()
hex_var.set(r3_hex)

text = Entry(root, textvariable=hex_var, fg=r3_hex, font='Helvetica 10 bold', bd=1, relief="groove", state="readonly",
             width=8, justify=CENTER)
text.insert(0, r3_hex)
text.pack()

root.mainloop()
