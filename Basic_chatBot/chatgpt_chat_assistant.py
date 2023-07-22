import openai

openai.api_key = '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'

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})
message = ''
print("Your new assistant is ready!")
while message != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")