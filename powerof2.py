#Question 3: Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.
#Examples:
#8=> returns true
#6=> returns false
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