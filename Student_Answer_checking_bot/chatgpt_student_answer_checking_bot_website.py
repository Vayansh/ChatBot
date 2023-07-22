import openai
import gradio
from huggingface_hub import (
    create_repo,
    get_full_repo_name,
    upload_file,
)

openai.api_key = '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'
messages = [{
    'role' : 'system',
    'content': ' Helpful Assistant'
}]

def studentAnswer_checker(Question,Student_answer):
    prompt = f"""Your task is to determine if the student's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem.
- Then compare your solution to the student's solution \
and evaluate if the student's solution is correct or not.
Don't decide if the student's solution is correct until
you have done the problem yourself.

Use the following format:
Question:

Student's solution:

Your solution:

Is the student's solution the same as actual solution \
just calculated:
```
yes or no
```
Student grade:
```
correct or incorrect
```

Question:
```
{Question}
```
Student's solution:
```
{Student_answer}
```
"""

    messages.append({'role':'user','content':prompt})
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = messages
    )
    reply = response['choices'][0]['message']['content']
    messages.append({'role':'assistant','content':reply})
    return reply

demo = gradio.Interface(fn = studentAnswer_checker,inputs = ['text','text'],outputs='text',title='Answer Checker')
demo.launch(share= True)
