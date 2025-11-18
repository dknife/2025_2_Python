import customtkinter as ctk

def change_label():
    if label.cget('text') == "안녕하세요!":
        label.configure(text="어서 오세요")
    else:
        label.configure(text="안녕하세요!")

app = ctk.CTk()
app.geometry("400x300")
app.title("CustomTkinter Example")

label = ctk.CTkLabel(app, text="안녕하세요", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=20)

button = ctk.CTkButton(app, text="Click Me", command=change_label)
button.pack(pady=10)

app.mainloop()
