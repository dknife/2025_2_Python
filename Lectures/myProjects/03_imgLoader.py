import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
# PIL은 pip install Pillow로 설치할 수 있습니다.

photo_image = None  # 전역 변수로 이미지 참조 유지

def load_image(path):
    img = Image.open(path)
    photo_image = ImageTk.PhotoImage(img)
    img_label.configure(image=photo_image, text="")

def open_image():
    path = filedialog.askopenfilename(title="Select an Image",
                               filetypes=[("Image Files", "*.png;*.jpg *.jpeg *.bmp  *.gif")])
    
    load_image(path)
    
    
# 껍데기를 만들자
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x500")
root.title("Image Loader")

img_label = ctk.CTkLabel(root, text="No image loaded")
img_label.pack(pady=20)

btn_frame = ctk.CTkFrame(root)
btn_frame.pack(pady=10)

open_btn = ctk.CTkButton(btn_frame, text="Open Image",
                         command=open_image)
open_btn.pack(side="left", padx=10)

root.mainloop()

