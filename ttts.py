import pyttsx3

def announce_offline(word):
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Announce the word
    engine.say(word)

    # Wait for the speech to finish
    engine.runAndWait()

# Example usage
word_to_announce = "ayeii! baigan?"
announce_offline(word_to_announce)
