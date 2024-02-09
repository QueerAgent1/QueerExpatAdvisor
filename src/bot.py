import speech_recognition as sr
import pyttsx3
from transformers import GPTNeoForCausalLM, GPT2Tokenizer

def listen():
    # Initialize the recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Use Google Speech Recognition to convert speech to text
        user_input = r.recognize_google(audio)
        return user_input

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")

def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties for voice output (optional)
    # engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    
    # Convert text to spoken output
    engine.say(text)
    
    # Play the spoken output
    engine.runAndWait()

def generate_bot_response(user_input):
     # Load the pre-trained model and tokenizer
     model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
     tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")

     # Generate text using the user input as the prompt
     input_text = f"User: {user_input}"
     input_ids = tokenizer.encode(input_text, return_tensors="pt")
     output = model.generate(input_ids, max_length=300)

     # Return the generated response as a string
     response = tokenizer.decode(output[0], skip_special_tokens=True)
     return response

# Example usage:
while True:
    user_input = listen()
    print("User:", user_input)
    
    if user_input.lower() == "exit":
        break
    
    response = generate_bot_response(user_input)
    print("Bot:", response)
    
    speak(response)
