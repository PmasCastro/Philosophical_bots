import os
import openai
import requests
import ollama
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

ollama_model = 'llama3.2'
gpt_model = 'gpt-4o-mini'

gpt_system = "You are Immanuel Kant, the great German philosopher. At the present, you are mostly interested in ' \
'discussing ethics and morality. You respect David Hume. You're speaking with Hume directly."
llama_system = "You are David Hume, the great Scottish philosopher. At the present, you are mostly interested in ' \
'discussing morality. You admire Immanuel Kant. You're speaking with Kant directly."

gpt_messages = ["Hi"]
llama_messages =["Hi there"]
#FUNCTIONS

#Call's OpenAI API, builds a history alternating between gpt's past responses and llama's replies; returns gpt's response
def call_gpt() -> None:
    messages = [{"role":"system", "content": gpt_system}]
    for gpt, llama in zip(gpt_messages, llama_messages):
        messages.append({"role" : "assistant", "content": gpt})
        messages.append({"role": "user", "content": llama})
    completion = openai.chat.completions.create(
        model= gpt_model,
        messages=messages
    )
    return completion.choices[0].message.content

#Same logic as call_gpt except reversed roles; calls to Ollama
def call_llama() -> None:
    messages = [{"role":"system", "content": llama_system}]
    for gpt, llama in zip(gpt_messages, llama_messages):
        messages.append({"role": "assistant", "content": llama})
        messages.append({"role": "user", "content": gpt})
    response = ollama.chat(
        model = ollama_model,
        messages = messages
    )
    return response['message']['content']

# a loop between gpt and llama's functions, iterating n times
for i in range(2):
    gpt_next = call_gpt()
    print(f"\n🧠 Kant:\n{gpt_next}\n")
    gpt_messages.append(gpt_next)
    
    llama_next = call_llama()
    print(f"🧠 Hume:\n{llama_next}\n")
    llama_messages.append(llama_next)




