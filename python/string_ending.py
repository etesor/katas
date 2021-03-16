# Write a function that returns True if a string ends with the second string.
# Example:
#   s1 = 'Hello world.'
#   s2 = 'world.'
#   Output = True

def endswith_it(string, ending):
    return string.endswith(ending)


print(endswith_it('hello', 'd'))