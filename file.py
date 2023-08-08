import re

def extract_words(text):
    pattern = r'\[([^\]]+)\]'  # Regular expression pattern to match words inside square brackets
    matches = re.findall(pattern, text)
    return matches

input_text = "Once upon a time, in a [adjective] [noun] far away, there lived a [adjective] [noun]."
word_array = extract_words(input_text)
print(word_array)
