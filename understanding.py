input_text = "my name is {Fareed} and i am a good pers"
segments = input_text.split('{')
segment = segments.split('}')
print(segment)
translated_segments = []

for segment in segments:
    if '}' in segment:
        # Preserve text within curly brackets
        preserved_text, remaining_text = segment.split('}', 1)
        translated_segments.append(preserved_text + '}' + remaining_text)
    else:
                # Translate text outside curly brackets
        # translated_input = tokenizer(segment, return_tensors="pt", truncation=True)
        # translation = model.generate(**translated_input)
        # translated_segment = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
        # translated_segments.append(translated_segment)
        print("verynice")