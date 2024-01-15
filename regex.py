import re

text = "the prices is $12.99."

# Using \d+ to find one or more digits
matches = re.findall(r'\d+', text)

print(matches)


#import re

# Example: Matching a specific word using re.compile()
text = "The quick brown fox jumps over the lazy dog."

# Compile the regex pattern
pattern = re.compile(r'\bfox\b')

# Use the compiled pattern to search for a match
match = pattern.search(text)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")
