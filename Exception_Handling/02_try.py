'''
#Catch Single Exception
try:
    x = 1/0
except ZeroDivisionError:
    print('Something went wrong!')

'''
# Catch Multiple Exceptions
try:
    x = 1/0
except ZeroDivisionError:
    print('Attempt to divide by zero')
except:
    print('Something else went wrong')
