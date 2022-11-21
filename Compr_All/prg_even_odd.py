
l1 = [1,2,3,4,5,6,7,8,9,10]
l_even = []
l_odd = []
for a in l1:
    if a%2==0:
        l_even.append(a)
    else:
        l_odd.append(a)

print(l1)
print(l_even)
print(l_odd)

s1 = {1,2,3,4,5,6,7,8,9,10}
s_even = {}
s_odd = {}

for i in s1:
    if i%2 == 0:
        s_even.add(i)


print(s_even)


