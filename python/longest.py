# Given two strings, return a string with the longest sequence of characters ordered alphabetically using both input strings with no duplicates.
# Example:
#   a1 = 'aacb'
#   a2 = 'ffge'
#   output = 'abcefg'
 
def longest(a1, a2):
    longest_list = list(a1 + a2)
    longest = set(longest_list)
    return ''.join(sorted(longest))
    
