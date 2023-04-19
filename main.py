from tkinter import *
import string
import random

root = Tk()
root.geometry('400x200')

passStr = StringVar()
pass_len = IntVar()


def get_pass():
    pass1 = string.ascii_letters + string.digits
    password = ''

    for x in range(pass_len.get()):
        password = password + random.choice(pass1)
    passStr.set(password)


Label(root, text='Password generator', font='calibri 18 bold').pack()
Label(root, text='Enter the length of password ').pack(pady=9)
Entry(root, textvariable=pass_len).pack(pady=2)
Button(root, text='Generate password', command=get_pass).pack(pady=15)
Entry(root, textvariable=passStr).pack(pady=2)

root.mainloop()
