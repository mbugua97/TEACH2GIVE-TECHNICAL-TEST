#Question 5: Reverse Integer
#Write a program that takes an integer as input and returns an integer with reversed digit
#ordering.
#Examples:
#For input 500, the program should return 5.
#For input -56, the program should return -65.
#For input -90, the program should return -9.
#For input 91, the program should return 19.


"""My Solution algorithm
Step1:check if variable input is a negative value by checking if it is less than 0
step2: if step1 is true multiply my -1
step3: converting the integer to a string and revese the string
step4:converte the revesed string to an integer
step5: if variable was a negative multipy by -1 else return variable

"""

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
