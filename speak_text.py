import subprocess

def speak_word(word, voice='en', speed=150, pitch=50):
    try:
        # Use subprocess to call eSpeak
        subprocess.run(['espeak', '-v', f'{voice}', '-s', str(speed), '-p', str(pitch), word])
    except Exception as e:
        print(f"Error: {e}")

# Example usage
word_to_speak = "Hello my name is transo, how may i help you ?"
speak_word(word_to_speak, voice='en +f3', speed=140, pitch=40)
