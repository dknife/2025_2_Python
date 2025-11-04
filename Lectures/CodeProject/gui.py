import tkinter as tk
from tkinter import ttk
import requests


def greet(event=None):
    city = combo.get().strip()
    if city:
        url = f'https://wttr.in/{city}?format=3'
        try:
            weather = requests.get(url, timeout=10).text.strip()
            message = f"현재 {city}의 날씨는 {weather}"
        except Exception as e:
            message = f"오류: {e}"
    else:
        message = "도시를 선택하거나 입력하세요."

    result_label.config(text=message)
    print(message)


root = tk.Tk()
root.title("City Weather (Dropdown)")

# 레이블
tk.Label(root, text="도시를 선택하거나 입력하세요:").pack(padx=10, pady=(10, 0))

# 드롭다운 (Combobox)
cities = [
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon",
    "Gwangju", "Suwon", "Ulsan", "Jeju", "London",
    "New York", "Tokyo", "Paris", "Sydney", "Beijing"
]
combo = ttk.Combobox(root, values=cities, width=28, state="normal")
combo.pack(padx=10, pady=5)
combo.focus()

# 버튼
tk.Button(root, text="날씨 보기", command=greet).pack(padx=10, pady=5)

# 결과 라벨
result_label = tk.Label(root, text="", fg="blue", wraplength=400)
result_label.pack(padx=10, pady=(5, 10))

# 엔터 키 바인딩
root.bind("<Return>", greet)

if __name__ == "__main__":
    root.mainloop()