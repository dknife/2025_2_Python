import customtkinter as ctk
import ollama

def ask_ollama():
    # prompt 박스에서 텍스트 가져오기
    prompt = prompt_box.get("1.0", "end").strip()
    print(prompt) # debugging line
    response = ollama.generate(model="llama3", prompt=prompt)
    output_box.delete("1.0", "end")  # 이전 출력 지우기
    output_box.insert("1.0", response['response'])  # 새 응답

app = ctk.CTk()
app.geometry("400x600")
app.title("Chatbot Interface")

prompt_box = ctk.CTkTextbox(app, width=380, height=200)
prompt_box.pack(pady=20)

ask_button = ctk.CTkButton(app, text="Ask AI",
                           command=ask_ollama)
ask_button.pack(pady=10)

output_box = ctk.CTkTextbox(app, width=380, height=300)
output_box.pack(pady=20)

app.mainloop()