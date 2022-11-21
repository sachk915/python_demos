
# With for loop
#Sqaures
sqaures = [i**2 for i in range(1,11)]
print(sqaures)

#Negative numbers
negative = [-i for i in range(1,11)]
print(negative)

# with If
even_nums = [i for i in range(1,11) if i%2 == 0]
odd_nums = [i for i in range(1,11) if i%2 != 0]
print(even_nums)
print(odd_nums)


#with if else
nums = (1,2,3,4,5,6,7,8,9,10)

num = [i*2 if(i%2 == 0) else -i for i in nums]
print(num)
