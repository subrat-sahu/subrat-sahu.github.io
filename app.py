# -*- coding: utf-8 -*-
from chatterbot import ChatBot
chatbot = ChatBot("Aryaman")
from chatterbot.trainers import ListTrainer

conversation=[
	"Hello",
	"Hi there!",
	"How are you doing?",
	"I'm doing great.",
	"That is good to hear",
	"Thank you",
	"You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("Hi!")
print(response)
