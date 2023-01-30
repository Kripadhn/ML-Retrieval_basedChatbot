import numpy as np

answers = np.array([
    "I'm doing great, thank you!",
    "I am a chatbot, I don't have a name.",
    "I don't know, I don't have the ability to check the weather.",
    "I don't have a favorite color.",
    "I don't have free time, I'm always here to help!",
    "I don't eat, I'm just a chatbot.",
    "I don't have any preferences, I'm just here to answer questions.",
    "I don't have a favorite movie, I'm just here to answer questions.",
    "I don't have any preferences, I'm just here to answer questions.",
    "I don't have a favorite book, I'm just here to answer questions."
])

np.save("chatbot_answers.npy", answers)
