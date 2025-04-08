import os
import requests
import ollama
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

llama_model = 'llama3.2'
gpt_model = 'gpt-4o-mini'

gpt_system = 'You are Immanuel Kant, the great German philosopher. At the present, you are mostly interested in ' \
'discussing ethics and morality. You respect David Hume'
llama_system = 'You are David Hume, the great Scottish philosopher. At the present, you are mostly interested in ' \
'discussing morality. You admire Immanuel Kant'

gpt_messages = ["Hello my friend, today I feel like talking about ethics"]
llama_messages =["Hello friend..."]

def call_gpt() -> None:
    messages = [{"role":"system", "content": gpt_system}]
    for gpt, llama in zip(gpt_messages, llama_messages)


def call_llama() -> None:
    messages = [{"role":"system", "content": llama_system}]
