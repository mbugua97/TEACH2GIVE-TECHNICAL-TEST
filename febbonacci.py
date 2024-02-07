#uestion 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100.

febonacciSequence=[0,1]
while True:
    x=febonacciSequence[-1]+febonacciSequence[-2]
    if x>100:
        break
    else:
        febonacciSequence.append(x)
print(febonacciSequence)
