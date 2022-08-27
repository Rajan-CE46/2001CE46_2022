def fact(x):
    return 1 if(x == 1 or x == 0) else x*fact(x-1)

x = int(input("Enter the number:\n"))
print('Value of', x,'factorial is', fact(x),'.')
