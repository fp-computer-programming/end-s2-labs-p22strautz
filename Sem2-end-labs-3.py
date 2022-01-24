# Author: SCT (AMDG) 1/24/12
# "Vowel remover"

def shortcut(s): #defining the function
    for vowel in "aeiou": # setting variable for vowels to compare
        s = s.replace(vowel, "") # if input includes vowle replace with blank
    return s # return result to function

# Test Cases
print(shortcut("here"))
print(shortcut("helicopter"))
print(shortcut("train"))