#defining each function and using return function
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
#taking input about operation to be performed
print("Please Select Operation: " "\n", "1: Addition" "\n", "2: Substraction" "\n", "3: Multiplication" "\n", "4: Division")
while True:
    operation=input("Enter Operation(1/2/3/4): ")
    if operation in ("1","2","3","4"):
        number1=float(input("Please enter first Number: "))
        number2=float(input("Please enter second Number: "))

        if operation=="1":
            print(number1,"+",number2,"=",add(number1,number2))
        elif operation=="2":
            print(number1,"-",number2,"=", substract(number1, number2))
        elif operation=="3":
            print(number1,"x",number2,"=", multiply(number1, number2))
        elif operation=="4":
            print(number1,"/",number2,"=", divide(number1, number2))
        break
    else:
        print("Invalid input")
