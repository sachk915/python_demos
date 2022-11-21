# Tuples are immutable
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# Methods

#index
print(days[2])

#Range of index
print(days[1:4])

# length
print(len(days))

#join
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1+t2)


print(days.count("Monday"))

# Existing item
t3 = ('a', 'b', 'c', 'd', 'e')
if 'a' in t3:
    print("a is present.")
else:
    print("a is absent.")




