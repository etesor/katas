# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples:

# number([]) # => []
# number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]


def number(lines):
    counter = 1
    output = []
    for i in range(len(lines)):
        line = str(i + 1) + ': ' + lines[i]
        output.insert(i, line)
    return output

a = list('Hellow')

print(number(a))
