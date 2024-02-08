#Question 3: Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.
#Examples:
#8=> returns true
#6=> returns false

"""My solution algorithm
step1:iterate through the powers of 2
step2:check if varable is equal to the iterate
step3: if step 2 is true then the variable is a power of 2
step4: if step 2 is false and the iterate  is greater than the varable return False

"""

def FindPower(number):
    count=1
    while True:
        a=2**count
        if a == number:
            return True
        if a > number:
            return False
        count+=1

print(FindPower(5))