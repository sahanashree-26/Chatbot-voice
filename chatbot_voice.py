import nltk
from nltk.chat.util import Chat, reflections
import pyttsx3  
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
pairs = [
    [r"hi|hello", ["Hello!", "Hi there!"]],
    [r"my name is (.*)", ["Nice to meet you, %1!"]],
    [r"what is your name\??", ["I'm a chatbot with a voice!"]],
    [r"bye", ["Goodbye!"]],
    [r"(.*)", ["Hmm... can you ask that differently?"]],
]

chatbot = Chat(pairs, reflections)
print("Chatbot: Hello! Type 'bye' to exit.")
speak("Hello! Type bye to exit.")

while True:
    user_input = input("> ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye!")
        speak("Goodbye!")
        break

    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    speak(response)
input("Press Enter to exit...")
