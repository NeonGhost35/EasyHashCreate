import hashlib
from tkinter import *


def clicked():
    userpass = txt.get()
    useralg = txt2.get()
    hashtext = ("hash.txt")
    hashtxt = open(hashtext,"w",encoding='utf-8', errors='ignore')
    hashpass = hashlib.new (useralg)
    hashpass.update (userpass.encode("utf-8"))
    hash1 = hashpass.hexdigest()
    hashtxt.write(hash1)
    res = ("Your Hash saved to hash.txt")
    lbl3.configure (text = res)

window = Tk()
window.title("HashCreater v 1.0")

lbl = Label(text = "Welcome!")
lbl.grid(column = 0, row = 1)

lbl1 = Label(text = "Input Key: ")
lbl1.grid(column = 0, row = 3)

lbl2 = Label(text = "Input Algorithm: ")
lbl2.grid(column = 0, row = 4)

lbl3 = Label(text = "")
lbl3.grid(column = 0, row = 6)

txt = Entry(window, width=20)
txt.grid(column = 1, row = 3 )

txt2 = Entry(window, width=20)
txt2.grid(column = 1, row = 4 )

btn = Button(window, text = "Create Hash", command=clicked, width = 10)
btn.grid(column= 1, row = 7)

window.geometry('400x250')
window.mainloop()