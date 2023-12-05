from transformers import MarianMTModel, MarianTokenizer

def translate_text_marian(input_text, target_language):
    """
    Translates the given input text to the specified target language using MarianMT model.
    Text within curly brackets is excluded from translation.

    Parameters:
    - input_text: The text to be translated.
    - target_language: The target language name (e.g., 'hindi').

    Returns:
    - The translated text.
    """
    model_name = f'Helsinki-NLP/opus-mt-en-{target_language}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    try:
        # Identify and exclude text within curly brackets
        segments = input_text.split('{')
        translated_segments = []

        for segment in segments:
            if '}' in segment:
                # Preserve text within curly brackets
                preserved_text, remaining_text = segment.split('}', 1)
                translated_segments.append(preserved_text + '}' + remaining_text)
            else:
                # Translate text outside curly brackets
                translated_input = tokenizer(segment, return_tensors="pt", truncation=True)
                translation = model.generate(**translated_input)
                translated_segment = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
                translated_segments.append(translated_segment)

        translated_text = ''.join(translated_segments)
        return translated_text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None

# Example usage:
input_text = "Hello, how are you? {This part should not be translated.} How is the weather?"
target_language_name = 'hi'

translated_text = translate_text_marian(input_text, target_language_name)

if translated_text:
    print(f"Original Text: {input_text}")
    print(f"Translated Text ({target_language_name}): {translated_text}")
