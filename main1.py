from transformers import MarianMTModel, MarianTokenizer

def translate_text_marian(input_text, target_language):
    """
    Translates the given input text to the specified target language using MarianMT model.

    Parameters:
    - input_text: The text to be translated.
    - target_language: The target language code (e.g., 'hi' for Hindi).

    Returns:
    - The translated text.
    """
    model_name = f'Helsinki-NLP/opus-mt-en-{target_language}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    try:
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True)
        translation = model.generate(**inputs)
        translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
        return translated_text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None

# Example usage:
input_text = input("enter what you want :")
# target_language_code = 'hi'  # 'hi' is the language code for Hindi

translated_text = translate_text_marian(input_text, "mr")

if translated_text:
    print(f"Original Text: {input_text}")
    print(f"Translated Text : {translated_text}")
