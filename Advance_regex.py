import re

text = "the location of the event is london and it's a great place"

match = re.search(r"location.*(london|berlin|madrid)", text)

if match:
  location = match.group(1)
  print(f"Found location: {location}")
else:
  print("No matching word found")


#import re

text = "My name is John"

match = re.search(r"^My name is (\w+)", text)

if match:
    name = match.group(1)
    print(f"Found name: {name}")
else:
    print("No name found.")


Character ranges
Character ranges can be used to match a single character against a set of possibilities. Let’s look at a couple of examples:

r”[A-Z] This will match a single uppercase letter.

r”[0-9$-,.] This will match any of the digits zero through nine, or the dollar sign, hyphen, comma, or period.

The two examples above are often combined with the repetition qualifiers. Let’s look at one more example:

r”([0-9]{3}-[0-9]{3}-[0-9]{4})”

This line of code will match a U.S. phone number such as 888-123-7612.