try:
    num1= int(input("Enter first number: \n"))
    num2 = int(input("Enter second number: \n"))

    operate =(input("Choose +, -,/,*"  ))
    match operate:
        case"+":
            print(f"sum : {num1+num2}")
            
        case"-":
            print(f"sub: {num1-num2}")
            
        case"/":
            if num2==0:   
                print(f"cannot divide by zero.")
            else:
                print(f"Division: {num1/num2}")  
        case("*"):
            print(f"Multiplication: {num1*num2}")    
        case _:
            print("Invalid operator")                
except ValueError:
    print("please enter vaild whole numbers.")
finally:
    print("Thank you!!")                