s = {"a", "b", "c"}
print("a" in s)

for i in s:
    print(i)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = {6,5,8,9,2}

print(s1 | s2)
print(s1 & s2)

#s3.update(0,1)
s3.update([4,3])
print(s3)
