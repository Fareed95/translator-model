import speech_recognition as sr
import pyttsx3
import keyboard

# Initializing the recognizer
r = sr.Recognizer()

def speak_text(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Loop
while True:
    try:
        # Use the microphone for input
        with sr.Microphone() as source:
            # Wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(source, duration=0.3)

            # Listen to the input from the user
            print("Listening ...")
            
            # Check if the 's' key is pressed to stop the process
            if keyboard.is_pressed('s'):
                print("Listening stopped by user.")
                break
            
            audio = r.listen(source)

            # Using Google to recognize audio
            my_text = r.recognize_google(audio)
            my_text = my_text.lower()

            print("Did you say: " + my_text)
            speak_text(my_text)

    except sr.RequestError as e:
        print("Could not request result; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")
