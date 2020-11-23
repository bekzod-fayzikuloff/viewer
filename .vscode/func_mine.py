from tkinter import *



def swipe():
    if btn['text'] =='hi':
        btn['text'] = 'bitch'
    else:
        btn['text'] = 'hi'



root = Tk()


btn = Button(root,text = 'hi',command = swipe)
btn.pack()
root.mainloop()