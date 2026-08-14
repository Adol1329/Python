try:
    num1= int(input("Enter first number: !\n"))
    num2 = int(input("Enter second number: \n"))
    sum=num1+num2
    sub=num1-num2
    division=num1/num2
    multiple=num1*num2
    print("1 sum")
    print("2 sub")
    print("3 divide")
    print("4 Mult")
    option = int(input("Choose btn (1,2,3,4):)"))
    match option:
        case(1):
            print(f"the sum of two numbers : {sum}")
            
        case(2):
            print(f" the subraction of two numbers: {sub}")
            
        case(3):
            print(f" the result  of two numbers: {division}")
        case(4):
            print(f" the Multiplication of two numbers: {multiple}")    
            
except:
    print("hello")            