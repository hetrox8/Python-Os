import re

text =  "This is a sentence. And here is another one? The last one!"

sentences = re.split(r"[.?!]",text)

sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

print(sentences)