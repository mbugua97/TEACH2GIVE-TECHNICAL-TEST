#Write a program that takes an integer as input and returns an integer with reversed digit
#ordering.
#Examples:
#For input 500, the program should return 5.
#For input -56, the program should return -65.
#For input -90, the program should return -9.
#For input 91, the program should return 19.

def ReverseNumber(number):
    if number < 0:
       number*=-1
       return(int(str(number)[::-1])*-1)
    
    else :
        return(int(str(number)[::-1]))

print(ReverseNumber(500))
print(ReverseNumber(-56))
print(ReverseNumber(-90))
print(ReverseNumber(91))