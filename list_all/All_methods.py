lst1=[1, 2, 3, 4, 5, 'a', 'b', 'c']
ls2 =[1, 2, 10, 12, 14, 3, 4, 5]
#Accessing Values in Lists
print(lst1[2])

# Updating Lists
lst1[2] ="PST"
print(lst1)

# Delete List Elements
del(lst1[1])
print(lst1)

# Total size of list
print(len(lst1))

#min and max function
print(max(ls2))
print(min(ls2))

# Add element in list
ls2.append(44)
print(ls2)

#remove element
ls2.remove(5)
print(ls2)

#reverse list
ls2.reverse()
print(ls2)