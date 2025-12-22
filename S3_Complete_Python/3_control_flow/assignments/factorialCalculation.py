#### Assignment 12: Factorial Calculation
#Write a program that calculates the factorial of a number input by the user using a while loop.

while True:
    stringInput=input("Digit a number: ")
    fatorial=1
    if stringInput.isnumeric:
        number=int(stringInput)

        if number>=0:
            if number==0 or number==1:
                print(f"The factorial of {number} is {1}")
            else:
                count=number
                while count>1:
                    fatorial=fatorial*count
                    count=count-1
                print(f"The factorial of {number} is {fatorial}")


        else:
            print(f"{number} is a negative number. A does not exist the fatorial of a negative number!")   
    else:
        print(f"{stringInput} is not a number.")