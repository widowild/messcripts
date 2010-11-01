from tkinter import *
from random import *
import string
 
# The characters to make up the random password
chars = string.ascii_letters + string.digits
 
def random_password():
    """ Create a password of random length between 8 and 16
        characters long, made up of numbers and letters.
    """
    return "".join(choice(chars) for x in range(randint(8, 16)))
 
#
# BEGIN GUI CODE
#
 
root = Tk()
root.title("Password Generator")
root.resizable(0,0)
root.minsize(300,0)
 
frame = Frame(root)
frame.pack(pady=10, padx=5)
 
content = StringVar()
updater = lambda:content.set(random_password())
 
gen_btn = Button(frame, text="Generate", command=updater)
gen_btn.config(font=("sans-serif", 14),  bg="#92CC92")
gen_btn.pack(side=LEFT, padx=5)
 
field = Entry(frame, textvariable=content)
field.config(fg='blue', font=('courier',  16, "bold"), justify='center')
field.pack(fill=BOTH, side=RIGHT, padx=5)
 
root.mainloop()
