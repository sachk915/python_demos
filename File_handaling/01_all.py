'''

# 1. Read a File
f = open("sample.txt", "r")
print(f.read())

#--------------------------------




# 2. Read Only Parts of the File
f = open("sample.txt", "r")
print(f.read(10))  # return number of words
'''

#-------------------------------

'''
# 3. Read Lines
f = open("sample.txt", "r")
print(f.readline(3))
'''

f1 = open("sample.txt", "r")
print(f1)

#---------------------------
'''
# 4. Write to an Existing File
f = open("sample.txt", "a")
f.write(" \n Now the file has more content!")
f.close()

f = open("sample.txt", "r")
print(f.read())

'''
#----------------------------------

# 5. Overwrite the content


'''
#--------------------------------

# 6. Create a New File1
f = open("myfile1.txt", "x")
'''
# -----------------------------------
'''
# 7.Delete a File
import os
os.remove("myfile.txt")
'''