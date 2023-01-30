import numpy as np

questions = np.array([
    "How are you today?",
    "What's your name?",
    "What's the weather like today?",
    "What's your favorite color?",
    "Do you have any free time?",
    "What's your favorite food?",
    "Do you have any preferences?",
    "What's your favorite movie?",
    "What are your hobbies?",
    "What's your favorite book?"
])

np.save("chatbot_questions.npy", questions)
