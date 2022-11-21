
try:
    x = 1/1
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('Always execute this')


# Finally
try:
    x = 1/0
except:
    print('Something went wrong')
finally:
    print('Always execute this')