# Program to extract numbers from a string

import re

string = 'hello 12 hi 89. How are you 34'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)

# Output: ['12', '89', '34']