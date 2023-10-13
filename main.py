import os
import openai
import fastapi
from pydantic import BaseModel
from fastapi import FastAPI,Form,Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import re
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key



class Usertext(BaseModel):
    Text: str

# Define CORS settings
origins = ["*"]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/keyword')
async def keyword(data: Usertext):
    Text = data.Text
    category_prompt = f"""Classify the following text into a category:\{Text}"""
    
    # Create a prompt for keyword extraction
    keywords_prompt = f"""Extract the top 15 keywords from the following text:\n{Text}"""
    
    # Make an API call for category classification
    category_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=category_prompt,
        max_tokens=1000,  
        api_key=api_key
    )

    # Make an API call for keyword extraction
    keywords_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=keywords_prompt,
        max_tokens=1000,  
        api_key=api_key
    )

    # Extract the category and keywords from the responses
    category = category_response["choices"][0]["text"].strip()
    keywords = keywords_response["choices"][0]["text"].strip()

    print("Category:", category)
    print("Keywords:", keywords)

    return {"category": category, "keywords": keywords}