
# Looping in tuple
mixed = (1,2,3,4.0)
print(type(mixed))
for i in mixed:
    print(i)


#Tuple with one element
x = (1)
print(type(x))


tupel_with_one_variable = (1,)
print(type(tupel_with_one_variable))


#Tuple without parenthesis
bikes = "Yamaha", "Honda", "Suzuki", "Maruti", "12222"
print(type(bikes))
print(bikes)

#Tuple unpacking
bikes = "Yamaha", "Honda", "Suzuki", "Maruti"
biker1, biker2, biker3, biker4 = (bikes)
print(biker1, biker2)
print(type(biker1))

print(bikes)

#List inside tuple
mixed_tuple = ("Attack on titan", "Death Note", ["Lucifer", "Money Heist", "Thor"])
print(mixed_tuple)
remove_ele = mixed_tuple[2].pop()
print("Remove element :- "+ remove_ele)
print(mixed_tuple)
mixed_tuple[2].append("Mirzapur")
print(mixed_tuple)


#Some functions
mixed = (1,2,3,4.0)
print(min(mixed))
print(max(mixed))
print(sum(mixed))

