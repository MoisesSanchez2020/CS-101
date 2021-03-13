
number = 1 
while number <= 10:
    print(f"The number is:{number}")

    number = number + 1
    print("Finish with the loop")




# BAD EXAMPLE: This code does not define a value for the number before it is used
while number < 10:
    number = int(input("what is the number?"))

    print("FInish woth the loop")






# GOOD EXAMPLE: This code correctly sets the variable to a value before it is used

number = 0

while number < 10:
    number = int(input("What is the number? "))

print("Finished with the loop")    


# BAD EXAMPLE: This code sets the variable to a number that prevents
# the code from ever entering the loop.

number = 25 # ERROR: This number is greater than 10, so the loop will not run

while number < 10: # This body of this loop will NEVER run
    number = int(input("What is the number? "))

print("Finished with the loop")    