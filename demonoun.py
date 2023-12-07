from transformers import MarianMTModel, MarianTokenizer
import math

def translate_text_marian(input_text, target_language):
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
                print(f'preser : {preserved_text}')
                print(f'remain : {remaining_text}')
                remain = translate_text_marian(remaining_text, 'hi')
                if not remain :
                    translated_segments.append(preserved_text)
                else :
                    translated_segments.append(preserved_text + remain)
                print(f'till here {translated_segments}')
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

input_text = input("enter what you want to :")
target_language_name = 'hi'

translated_text = translate_text_marian(input_text, target_language_name)

if translated_text:
    print(f"Original Text: {input_text}")
    print(f"Translated Text ({target_language_name}): {translated_text}")




















# Example usage:
