import pyttsx3
import os
import time

def text_to_speech(text, language, filename):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # You can adjust the speed
    engine.save_to_file(text, filename)
    engine.runAndWait()

if __name__ == "__main__":
    hindi_text = "नमस्ते, कैसे हो?"
    marathi_text = "नमस्कार, कसा आहे?"
    english_text = "hello "

    # Save to mp3 files
    text_to_speech(hindi_text, 'hi', 'hindi_output.mp3')
    text_to_speech(marathi_text, 'mr', 'marathi_output.mp3')
    text_to_speech(english_text,'en','english_output.mp3')
    # Wait for a moment to ensure the files are created
    time.sleep(2)

    # Play the generated audio files
    os.system('start hindi_output.mp3')
    os.system('start marathi_output.mp3')
    