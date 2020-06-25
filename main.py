#Chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Speech Recognition
import speech_recognition as sr

#Speech Synthesis
import pyttsx3

import os

logics = ["chatterbot.logic.TimeLogicAdapter"]

bot = ChatBot(
  'Lisa',
  storage_adapter='chatterbot.storage.SQLStorageAdapter',
  logic_adapters=[
    'chatterbot.logic.MathematicalEvaluation',
    'chatterbot.logic.TimeLogicAdapter',
    'chatterbot.logic.BestMatch'
    ]
)

trainer = ListTrainer(bot)

for file in os.listdir('chats'):
  chats = open('chats/' + file, 'r').readlines()
  trainer.train(chats)

# r = sr.Recognizer()

# with sr.Microphone() as s:
#   r.adjust_for_ambient_noise(s)

#   while True:
#     audio = r.listen(s)
#     speech = r.recognize_google(audio, language="pt-BR")

while True:
  request = input('Digite um texto: ')
  print('Bot: ' + str(bot.get_response(request)))