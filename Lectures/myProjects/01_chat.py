import ollama

def build_prompt():
    prompt = input("You: ")
    return prompt

def ask_ollama(prompt):
    response = ollama.generate(model="llama3", prompt=prompt)
    return response['response']

if __name__ == "__main__":
    prompt = build_prompt()
    response = ask_ollama(prompt)
    print(f"AI: {response}")
