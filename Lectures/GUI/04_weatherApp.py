import customtkinter as ctk
import requests

# GUI 테마 설정
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def get_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.configure(text="도시 이름을 입력하세요.")
        return  
    result_label.configure(text="날씨 정보를 가져오는 중...")
    app.update()

    # 날씨 가져오기
    url = f'https://wttr.in/{city}?format="%l:+%c+%t+%w+%p+%m'
    response = requests.get(url)
    if response.status_code == 200:
        weather_info = response.text.strip().strip('"')
        result_label.configure(text=weather_info)
    else:
        result_label.configure(text="날씨 정보를 가져오지 못했습니다.")

app = ctk.CTk()
app.geometry("400x300")
app.title("강영민의 날씨 프로그램")

city_label = ctk.CTkLabel(app, text="도시를 입력하세요:", font=ctk.CTkFont(size=16))
city_label.pack(pady=10)

# Entry 위젯 생성
city_entry = ctk.CTkEntry(app, 
                          placeholder_text="예: Seoul, Busan, Beijing, Ho Chi Minh",
                          width=300, font=ctk.CTkFont(size=14))
city_entry.pack(pady=10)

result_label = ctk.CTkLabel(app, text="날씨가 표시됩니다.", font=ctk.CTkFont(size=14))
result_label.pack(pady=10)

# 검색 버튼
btn = ctk.CTkButton(app, text="날씨 검색", width = 200, height= 50, command = get_weather)
btn.pack(pady=10)

app.mainloop()