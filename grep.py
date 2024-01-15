#this are terminal commands
#grep si.ng /home/downloads/
#this is used to check for words that have 'si' and 'ng'
  
#grep ^st /home/downloads/words
#to check words that start with 'st'

#grep st$ /home/downloads/words
#to check words ending with 'st'

import re
result = re.search(r'aza','plaza')
print(result)


#import re

results = re.search(r'ze','maze')
print(results)

print(r'^x','xenon')

#import re

output = re.search(r'p.ng','penguin')

print(output)

#import re
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))