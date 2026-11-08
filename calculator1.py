a=input(int("Enter first number: "))
b=input(int("Enter second number: "))
print("choose operation: " )
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=input("Enter choice(1/2/3/4): ")
if choice=='1':
    print(a,"+",b,"=",a+b) // Addition
elif choice=='2':
    print(a,"-",b,"=",a-b) // Subtraction
elif choice=='3':
    print(a,"*",b,"=",a*b) // Multiplication
elif choice=='4':
    print(a,"/",b,"=",a/b) // Floor division
else:
    print("Invalid input: please choose a valid operation") 
