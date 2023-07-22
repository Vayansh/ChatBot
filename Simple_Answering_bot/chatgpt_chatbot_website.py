import openai
import gradio

openai.api_key = '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'
messages = [{'role':'system','content': "You are a helpful assistant"}]

def CustomChatGPT(user_input):
    messages.append({'role':'user',"content":user_input})
    respone = openai.ChatCompletion.create(model = 'gpt-3.5-turbo',messages = messages)
    reply = respone['choices'][0]['message']['content']
    messages.append({'role': "assistant",'content':reply})
    return reply

demo = gradio.Interface(fn= CustomChatGPT,inputs= 'text',outputs='text',title='Helpful Assistant')
demo.launch()
    