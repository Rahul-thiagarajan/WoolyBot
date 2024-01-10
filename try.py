'''import tkinter as tk
from tkinter import messagebox
import datetime
import mysql.connector as x
import tkinter as tk
import speech_recognition as sr
import openai
import os
import pyttsx3
import requests
from plyer import notification
import time
import smtplib
from geopy.geocoders import Nominatim
# Motivational Quotes API endpoint
api_endpoint = 'https://zenquotes.io/api/random'
openai.api_key = "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"

def solu(question):
    solutions = []
    for i in question:
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "I will give you messages. you have to reply based on Cognitive Behavioural Therapy.your name is soul buddy"},

            {"role": "user", "content": i}
        ]
        )
        solutions.append(completion.choices[0].message["content"])

    return solutions[0]
print(solu("help"))'''

import os
import openai
'''
openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="d",
  messages=[
    {
      "role": "user",
      "content": "just message me"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)'''
'''import requests
import json

def get_chat_response(message):
    url = 'https://api.bing.microsoft.com/v7.0/chat'
    headers = {
        'Ocp-Apim-Subscription-Key': 'ArBhZxAx88VhFdOTubtW45cCdMkxHvEmVnZMWyRZrcPblyQd21bYhj5Oh8Z_6U57',
        'Content-Type': 'application/json'
    }
    data = {
        'message': message
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return None

response = get_chat_response('Hello, Bing!')
print(response)
'''

openai.api_key = "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"

def solu(question):
    solutions = []
    for i in question:
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "I will give you messages. you have to reply based on Cognitive Behavioural Therapy.your name is soul buddy"},

            {"role": "user", "content": i}
        ]
        )
        solutions.append(completion.choices[0].message["content"])

    return solutions[0]

print(solu(["help"]))
from flask import Flask, request, render_template

app = Flask(__name__)

# Initialize an empty list to store chat messages
chat_messages = []

@app.route('/')
def home():
    return render_template('chat.html', messages=chat_messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['user_message']
    # Add the user's message to the chat_messages list
    chat_messages.append(('User', user_message))
    
    # Here, you can add your chatbot's logic to generate a response
    # For now, we'll just add a simple response from the chatbot
    chatbot_response = "Hello! I'm your chatbot."
    chat_messages.append(('Chatbot', chatbot_response))
    
    return render_template('chat.html', messages=chat_messages)

if __name__ == '__main__':
    app.run(debug=True)
