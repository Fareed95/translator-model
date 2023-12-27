from demonoun import translate_text_marian
from speak_text import speak_word
import time

input_text = input("enter what you want to :")
# target_language_name = 'hi'

translated_text_hindi = translate_text_marian(input_text, 'hi')
translated_text_marathi = translate_text_marian(input_text, 'mr')


# if translated_text:

b = translated_text_hindi.replace("( तिरछे टाइप हमारे)","")
c = translated_text_marathi.replace("A button on a Remote Control","")
print(c)
    # print(b)
print(f"Original Text: {input_text}")
print(f"Translated hindi Text (): {b}")
print(f"Translated marathi Text (): {c}")

# word_to_speak = 
speak_word(input_text, voice='en +f5', speed=10, pitch=75)
time.sleep(2)
speak_word(b, voice='hi +f5', speed=10, pitch=75)
time.sleep(2)
speak_word(c, voice='hi +f5', speed=10, pitch=75)
# time.sleep(7)
