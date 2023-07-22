import openai

openai.api_key = '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'

completion = openai.ChatCompletion.create(model = 'gpt-3.5-turbo',messages = [{"role": "user", "content": "Write a essay on penguins."}])
print(completion.choices[0].message.content)