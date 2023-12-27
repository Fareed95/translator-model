import subprocess

def speak_word(word, voice='hi', speed=150, pitch=50):
    try:
        # Use subprocess to call eSpeak
        subprocess.run(['espeak', '-v', f'{voice}', '-s', str(speed), '-p', str(pitch), word])
    except Exception as e:
        print(f"Error: {e}")

# Example usage

