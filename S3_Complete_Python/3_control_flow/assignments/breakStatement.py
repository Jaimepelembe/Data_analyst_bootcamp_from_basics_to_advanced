### Assignment 8: break Statement
#Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.
total=0
while True:
    number=int(input("Press 0 (zero) to exit \nDigit a number: "))
    
    if number !=0:
        total=total+number
    else:
        break

print(f"The sum of all inputs is: {total}")
