### Assignment 15: Fibonacci Sequence
#Write a program that prints the first n Fibonacci numbers, where n is input by the user.

while True:
    stringInput=input("Digit a number: ")
    if stringInput.isnumeric:
        number=int(stringInput)
        firstTerm=0
        secondTerm=1
        fibonacci=0
        if number>=0:
            for i in range(number):
                fibonacci=firstTerm+secondTerm
                firstTerm=secondTerm
                secondTerm=fibonacci
            print(f"The fibonacci of {number} is {fibonacci}")
        else:
            print(f"{number} is negative and does not exist the fibonacci of a negative number")
            

    key=input("Press Q to exit: ")
    if key=="q" or key=="Q":
        break
