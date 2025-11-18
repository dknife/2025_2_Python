from tkinter import *

window = Tk()
window.title("BMI 계산기")
window.geometry("400x300")

label = Label(window, text="BMI 계산기 - 체중(kg)과 키(cm)를 입력하세요", 
              font=("Arial", 14))

Entry_weight = Entry(window, width=10, font=("Arial", 12))
Entry_height = Entry(window, width=10, font=("Arial", 12))

btn = Button(window, text="BMI 계산", font=("Arial", 12))

result_label = Label(window, text="BMI = ", font=("Arial", 12))   

btn.pack(pady=10)
label.pack(pady=20)
Entry_weight.pack(pady=5)
Entry_height.pack(pady=5)
result_label.pack(pady=10)

window.mainloop()