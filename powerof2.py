#finding if a number is  powers of 2
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