def longest(a1, a2):
    longest_list = list(a1 + a2)
    longest = set(longest_list)
    return ''.join(sorted(longest))
    
