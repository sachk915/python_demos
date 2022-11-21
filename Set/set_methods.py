s = {1,1.0,2.3,3,4.0,"string"}
print(s)
s.add("another string")
print(s)
s.discard("string")
print(s)
s.discard("stringsidsa")
print(s)


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
print(s1 | s2)
print(s1 & s2)