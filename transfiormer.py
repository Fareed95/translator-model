from main import translate_text
# Example usage:
input_text = input("enter what you want :")
# target_language_code = 'es'  # Change this to the language code you want

translated_texthi = translate_text(input_text, "hi")
print(f"hi : {translated_texthi}")
translated_text = translate_text(input_text, "mr")
print(f"mr : {translated_text}")