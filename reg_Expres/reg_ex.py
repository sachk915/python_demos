
import re

# 1. re.findall()
mystr = "at what time?"
match = re.findall('at',mystr)
print(match)

# 2. re.search()
string = "at what time?"
match = re.search('at', string)
if(match):
    print("String is found at: ", match.start())
else:
    print("String is not found!")

# 3. re.split() Function
txt = "India Country"
x = re.split("\s", txt)
print(x)

# 4. re.sub()
string = "python at PST 12345"
match = re.sub("\s",",", string)
print(match)

# ------------------------------------------------

# 1. [] – A set of characters
txt = "I am a Python Programmer"
x = re.findall("[a-e]", txt)
print(x)

# 2. \ – Signals a special sequence
x = re.findall("\Apython", string)
print(x)

# 3. ^ – Starts with
txt = "My Country is India"
x = re.findall("^My", txt)
if x:
    print("Yes, the string starts with ‘My'")
else:
    print("No match")


# 4. $ – Ends with
txt = "My Country is India"

#Check if the string ends with ‘India’:

x = re.findall("India$", txt)
if x:
    print("Yes, the string ends with 'India'")
else:
    print("No match")


# 5. | – Either or
txt = "India is my country and I love my country"

#Check if the string contains either “falls” or “stays”:

x = re.findall("my|is", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

