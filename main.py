import os
import requests
import ollama
from dotenv import load_dotenv
from openai import OpenAI

# load_dotenv('../.env')
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

llama_model= 'llama3.2'

