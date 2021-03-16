# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, they should be returned as they are. 
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
# Please note that using encode is considered cheating.
import string

def rot13(message):
    response = ''
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                index = string.ascii_lowercase.index(letter) + 13
                response += string.ascii_lowercase[index]
            else:
                index = string.ascii_uppercase.index(letter) + 13
                response += string.ascii_uppercase[index]        
        else:
            response += letter
    return response

message = 'This is a test script.'

# print(string.ascii_lowercase([1]))
print(rot13(message))