dick = {f"Square of {num} is":num**2 for num in range(1,11)}
for k, v in dick.items():
    print(f"{k} {v}")





name = "Rushikesh"
dit = {char1:name.count(char1) for char in name}
print(dit)

#with if
odd_even = {i:("even" if i%2==0 else "odd") for i in range(1,11)}
print(odd_even)

