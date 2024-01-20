import re

pattern = r"\[(\d+)\]"

text = "This is an example [123] with a PID inside brackets."

match = re.search(pattern, text)

if match:
  pid = match.group(1)
  print(f"pid extracted: {pid}")
else:
  print("no pid found")


#import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


#Here's a breakdown of the components:
#\[ - Matches the opening square bracket.
#(\d+) - Capturing group for one or more digits (\d+).
#\] - Matches the closing square bracket.