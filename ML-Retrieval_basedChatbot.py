import tensorflow as tf
import numpy as np

# Load the data
questions = np.load("chatbot_questions.npy")
answers = np.load("chatbot_answers.npy")

# Preprocess the data
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=200)
tokenizer.fit_on_texts(questions)
questions = tokenizer.texts_to_sequences(questions)
answers = tokenizer.texts_to_sequences(answers)
max_len = max([len(seq) for seq in questions])
questions = tf.keras.preprocessing.sequence.pad_sequences(questions, maxlen=max_len)

# Define the model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(200, 128, input_length=max_len))
model.add(tf.keras.layers.LSTM(128))
model.add(tf.keras.layers.Dense(200, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy')

# Fit the model to the data
model.fit(questions, answers, epochs=100, batch_size=32, verbose=0)

# Predict the response
response = model.predict(questions)
response = np.argmax(response)
print("Chatbot: ", tokenizer.sequences_to_texts(response))
