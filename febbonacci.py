#question 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100.

"""my solution algorithm
step1:declare an array with the first 2 variables of the Fibonacci sequence
step2: add the last 2 ellements in the array and append the resalt to the array
step3: repeat step2 till when the variabe result from adding the last 2 elements is greater than 100 
"""


febonacciSequence=[0,1]
while True:
    x=febonacciSequence[-1]+febonacciSequence[-2]
    if x>100:
        break
    else:
        febonacciSequence.append(x)
print(febonacciSequence)
