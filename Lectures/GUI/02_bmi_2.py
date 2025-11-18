from tkinter import *

def calculate_bmi():
    weight = float(Entry_weight.get())
    height = float(Entry_height.get())
    height = 180.0 / 100  # cm to m
    # bmi: 몸무게를 키의 제곱으로 나눈 값 (kg/m²)
    bmi = weight / (height * height)
    result_label.config(text=f"BMI = {bmi:.2f}")

window = Tk()
window.title("BMI 계산기")
window.geometry("400x300")

label = Label(window, text="BMI 계산기 - 체중(kg)과 키(cm)를 입력하세요", 
              font=("Arial", 14))

Entry_weight = Entry(window, width=10, font=("Arial", 12))
Entry_weight.insert(0, "kg")  # 기본값 설정
Entry_height = Entry(window, width=10, font=("Arial", 12))
Entry_height.insert(0, "cm")  # 기본값 설정

btn = Button(window, text="BMI 계산", font=("Arial", 12), command=calculate_bmi)

result_label = Label(window, text="BMI = ", font=("Arial", 12))   

btn.pack(pady=10)
label.pack(pady=20)
Entry_weight.pack(pady=5)
Entry_height.pack(pady=5)
result_label.pack(pady=10)

window.mainloop()