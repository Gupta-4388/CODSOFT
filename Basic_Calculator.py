def add(num1,num2):
    return num1 + num2 
    
def subtraction(num1,num2):
    return num1 - num2
    
def multiplication(num1,num2):
    return num1 * num2
    
def division(num1,num2):
    if num2==0:
        print("Error! Divison by zero.")
    return num1 / num2
    
def calculator():
    print("Select Operator:")
    print("1.Add")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    choice=input("Enter choice among (1/2/3//4): ")

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
           print("Result: ",add(num1,num2))
        elif choice == '2':
           print("Result: ",subtraction(num1,num2))
        elif choice == '3':
           print("Result: ",multiplication(num1,num2))
        elif choice == '4':
           print("Result: ",division(num1,num2))
    else:
           print("Enter valid choice")
calculator()
       
    
