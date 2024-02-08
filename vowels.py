#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.
#eg " Hello World " => returns 2


"""My solution algorithm
step1:have an array consiting of vowels
step2: iterate though the sentence finding the vowels and append to a hold list
step3: return count of distinct vowels found in step2 
"""
vowels=['a','e','i','o','u']
def CountVowels(sentence):
    found_vowels=[]
    for letter in sentence:
        if letter in vowels:
            found_vowels.append(letter)
    return len(set(found_vowels))
            

print(CountVowels("Hello World"))


        