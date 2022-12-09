
# ---------Special Sequences----------------------------------

# 1. \A
txt = "Python is a Lightweight Programming Language"
x = re.findall("\APython", txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match")


# 2. \D
txt = "India@123"
#Return a match at every no-digit character:

x = re.findall("\D", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# 3. \d
txt = "India@123"
#Return a match at every no-digit character:

x = re.findall("\d", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# 4. \S
txt = "A B C"
#Return a match at every NON white-space character:

x = re.findall("\S", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# 5. \s
xt = "I am a Python Programmer"


#Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


