n = int(input("Enter a number: "))
if n>=0 and n<=9:
    print("the square of the number is:", n*n)
elif n>9 and n<=99:
    print("the square root of the number is:", n**0.5)
elif n>99 and n<=999:
    print("the cube root of the number is:", n**(1/3))
else:
    print("the number is more than 3 digits")