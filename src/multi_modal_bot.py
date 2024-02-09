import speech_recognition as sr
import pyttsx3
from tkinter import Tk, Button, Text

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def process_text_input(text):
    # Process the text input from GUI or other sources
    # Add your logic here to generate a response based on the input
    
    return "Bot: This is a response to your text input."

def process_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Use Google Speech Recognition to convert speech to text
        user_input = recognizer.recognize_google(audio)
        
        # Process the voice input and generate a response
        response = process_text_input(user_input)
        
        print("User:", user_input)
        print(response)
        
        # Convert the bot's response to spoken output using text-to-speech engine
        engine.say(response)
        engine.runAndWait()
    
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    
    except sr.RequestError:
         print("Sorry, there was an issue with the speech recognition service.")

def handle_button_click():
    # Get the user's input from GUI and process it
    user_input = textbox.get(1.0, "end-1c")
    
    if user_input.strip() != "":
         response = process_text_input(user_input)
         textbox.insert("end", "\n\n" + response)

# Create GUI window using Tkinter library
window = Tk()
window.title("Multi-modal Bot")

# Create a button for voice interaction in the GUI
voice_button = Button(window, text="Voice Input", command=process_voice_input)
voice_button.pack()

# Create a text box for text-based interaction in the GUI
textbox = Text(window, height=10, width=50)
textbox.pack()

# Create a button to process the user's text input in the GUI
text_button = Button(window, text="Process Text Input", command=handle_button_click)
text_button.pack()

window.mainloop()
