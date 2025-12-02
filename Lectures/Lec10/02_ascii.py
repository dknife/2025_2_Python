import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from PIL import Image
import os
from datetime import datetime

# 최고 품질 아스키 문자 세트
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

# 전역 변수
현재_이미지_경로 = None
마지막_아스키 = ""

def 이미지_아스키로_변환(이미지경로, 너비):
    try:
        img = Image.open(이미지경로).convert("L")
        w, h = img.size
        비율 = h / w
        높이 = int(너비 * 비율 * 0.55)
        img = img.resize((너비, 높이), Image.Resampling.LANCZOS)
        pixels = list(img.getdata())
        
        # 안전한 인덱싱
        chars = []
        for p in pixels:
            idx = min(p * (len(ASCII_CHARS) - 1) // 255, len(ASCII_CHARS) - 1)
            chars.append(ASCII_CHARS[idx])
        
        lines = [''.join(chars[i:i+너비]) for i in range(0, len(chars), 너비)]
        return "\n".join(lines), (너비, len(lines))
    except Exception as e:
        return f"오류: {str(e)}", (0, 0)

def 파일_선택():
    global 현재_이미지_경로
    경로 = filedialog.askopenfilename(
        title="이미지 선택",
        filetypes=[("이미지", "*.png *.jpg *.jpeg *.bmp *.gif *.webp")]
    )
    if 경로:
        현재_이미지_경로 = 경로
        경로_라벨.config(text=f"선택됨: {os.path.basename(경로)}")
        실시간_변환()  # 바로 변환 시작

def 실시간_변환():
    if not 현재_이미지_경로:
        return
    
    결과_텍스트.config(state=tk.NORMAL)
    결과_텍스트.delete(1.0, tk.END)
    결과_텍스트.insert(tk.END, "변환 중...\n\n")
    결과_텍스트.update_idletasks()

    너비 = 슬라이더.get()
    아스키, 크기 = 이미지_아스키로_변환(현재_이미지_경로, 너비)
    
    결과_텍스트.delete(1.0, tk.END)
    결과_텍스트.insert(tk.END, f"파일: {os.path.basename(현재_이미지_경로)}\n")
    결과_텍스트.insert(tk.END, f"너비: {너비}자 | 높이: {크기[1]}줄\n")
    결과_텍스트.insert(tk.END, f"업데이트: {datetime.now().strftime('%H:%M:%S')}\n")
    결과_텍스트.insert(tk.END, "═" * 80 + "\n\n")
    결과_텍스트.insert(tk.END, 아스키)
    결과_텍스트.see(tk.END)
    결과_텍스트.config(state=tk.DISABLED)
    
    global 마지막_아스키
    마지막_아스키 = 아스키
    저장_버튼.config(state=tk.NORMAL)

def 저장하기():
    if not 마지막_아스키 or "오류" in 마지막_아스키:
        messagebox.showwarning("경고", "정상적으로 변환된 아스키 아트가 없습니다!")
        return
    저장경로 = filedialog.asksaveasfilename(
        defaultextension=".txt",
        initialfile=f"{os.path.splitext(os.path.basename(현재_이미지_경로 or 'ascii'))[0]}_ascii.txt"
    )
    if 저장경로:
        with open(저장경로, "w", encoding="utf-8") as f:
            f.write(f"아스키 아트 - 생성됨: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"원본: {os.path.basename(현재_이미지_경로) if 현재_이미지_경로 else '알 수 없음'}\n")
            f.write(f"너비: {슬라이더.get()}자\n\n")
            f.write(마지막_아스키)
        messagebox.showinfo("저장 완료!", f"저장됨!\n{저장경로}")

# GUI 생성
root = tk.Tk()
root.title("이미지 → 아스키 아트 변환기 - 실시간 미리보기")
root.geometry("1100x900")
root.configure(bg="#0d1117")

# 제목
tk.Label(root, text="이미지 → 아스키 아트 변환기", font=("Consolas", 22, "bold"),
         fg="#58a6ff", bg="#0d1117").pack(pady=20)

# 버튼들
프레임 = tk.Frame(root, bg="#0d1117")
프레임.pack(pady=10)

tk.Button(프레임, text="이미지 선택", font=("맑은 고딕", 14), width=15, height=2,
          bg="#238636", fg="white", command=파일_선택).pack(side=tk.LEFT, padx=10)
tk.Button(프레임, text="다시 변환", font=("맑은 고딕", 14), width=15, height=2,
          bg="#da3633", fg="white", command=실시간_변환).pack(side=tk.LEFT, padx=10)
저장_버튼 = tk.Button(프레임, text="저장하기", font=("맑은 고딕", 14), width=15, height=2,
                     bg="#8957e5", fg="white", command=저장하기, state=tk.DISABLED)
저장_버튼.pack(side=tk.LEFT, padx=10)

# 파일 라벨
경로_라벨 = tk.Label(root, text="선택된 파일: 없음", font=("Consolas", 11),
                     fg="#8b949e", bg="#0d1117")
경로_라벨.pack(pady=5)

# 슬라이더 (실시간 반영!)
슬라이더_프레임 = tk.Frame(root, bg="#0d1117")
슬라이더_프레임.pack(pady=15)

tk.Label(슬라이더_프레임, text="아스키 너비:", font=("Consolas", 14), fg="white", bg="#0d1117").pack(side=tk.LEFT, padx=10)
슬라이더 = tk.Scale(슬라이더_프레임, from_=50, to=250, orient=tk.HORIZONTAL, length=600,
                    command=lambda x: 실시간_변환() if 현재_이미지_경로 else None,
                    bg="#21262d", fg="#58a6ff", highlightbackground="#0d1117", troughcolor="#30363d")
슬라이더.set(120)
슬라이더.pack(side=tk.LEFT)

# 결과 영역
결과_텍스트 = scrolledtext.ScrolledText(root, font=("Consolas", 9), bg="#0d1117", fg="#7ee787",
                                       insertbackground="white", selectbackground="#1f6feb")
결과_텍스트.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# 초기 메시지
결과_텍스트.insert(tk.END, """
    ╔══════════════════════════════════════════════════════════════╗
    ║               실시간 아스키 아트 변환기 v3.0                 ║
    ║                                                              ║
    ║   이미지 선택 → 슬라이더 움직이면 바로 변환됨!              ║
    ║   [다시 변환] 버튼으로 강제 새로고침                        ║
    ║   저장하기 로 .txt 파일로 영구 보관                         ║
    ╚══════════════════════════════════════════════════════════════╝
""")
결과_텍스트.config(state=tk.DISABLED)

root.mainloop()