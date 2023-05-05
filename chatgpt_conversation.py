import openai
import os
import time

openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up the initial prompt
initial_prompt = "Hello, I am ChatGPT. What would you like to talk about?"

# Begin the conversation
print(initial_prompt)
messages = [{
            'role':'assistant',
            'content':initial_prompt
        }]

while True:
    prompt = input('\nAsk a question: ')    
    messages.append(
        {
            'role':'user',
            'content':prompt
        })    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages)
    
    response = completion['choices'][0]['message']['content']
    print(response)    
    messages.append(
        {
            'role':'assistant',
            'content':response
        })  