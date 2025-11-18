from tkinter import *

def change_label():
    if label.cget('text') == "안녕하세요!":
        label.config(text="어서 오세요", bg="green", fg="white")
    else:
        label.config(text="안녕하세요!", bg="yellow", fg="blue")


window = Tk()
label = Label(window, text="안녕하세요!", 
              bg="yellow", fg="blue", 
              font=("Arial", 24))

label.pack(padx=200, pady=200)

btn = Button(window, text="클릭해서 문자 변경", command= change_label)
btn.pack()
window.mainloop()