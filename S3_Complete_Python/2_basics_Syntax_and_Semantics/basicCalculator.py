#Basic calculator
while True:
    inputString=input("Insert number one: ")
    numberOne=float(inputString)
    inputString=input("Insert number two: ")
    numberTwo=float(inputString)

    print("Choose the operation: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5.Floor division \n 6. Modulus \n 7. Exponentiation ")
    inputString=input()
    operation=int(inputString)

    match operation:
        case 1:
            operationResult= numberOne+numberTwo
            print(operationResult)

        case 2:
            operationResult=numberOne-numberTwo
            print(operationResult)
        case 3:
            operationResult=numberOne*numberTwo
            print(operationResult)
    
        case 4:
            if numberTwo !=0:
                operationResult=numberOne/numberTwo
                print(operationResult)
            else:
                print("The denominator is 0. And it is impossible to divide by zero")
            
        case 5:
            if numberTwo !=0:
                operationResult=numberOne//numberTwo
                print(operationResult)
            else:
                print("The denominator is 0. And it is impossible to divide by zero")
        
        case 6:
            if numberTwo !=0:
                operationResult=numberOne%numberTwo
                print(operationResult)
            else:
                print("The denominator is 0. And it is impossible to divide by zero")
        
        case 7:
            if numberOne !=0 and numberTwo>=0:
                operationResult=numberOne**numberTwo
                print(operationResult)
            else:
                print("The denominator is 0. And it is impossible to divide by zero")
            
    print("Do you want to continue? \n 1.Yes \n 2. No")
    inputString=input()
    decision=int(inputString)
    if decision==2:
        break