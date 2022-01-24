# Author: SCT (AMDG) 1/24/12
# "Mumbling"

def accum(s): #Defining Function
    i = 0 # sets function that increases number of letters each time
    result = '' # Sets blank str to hold result
    for letter in s: # Sets loop that iterates each letter from input
        result += letter.upper() + letter.lower() * i + '-' # Sets result = to captialized letter chosen + lower case of the letter chosen times the iteration + dash 
        i += 1 # keeps track of each iteration
    return result[:len(result)-1] # returns total len of result -1 back to function

# Test Cases
print(accum("abcd"))
print(accum("hello"))
print(accum("cat"))
