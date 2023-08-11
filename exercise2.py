# Create a function that takes a string s as a parameter and returns another string where all
# the letters in s has been re-arranged such that upper case letters appear before the lower case
# letters.
# EX: if s is “Hello World”, the function returns “HWelloorld”.


########################################################################


# O(n) => n = total number of characters,

def rearrange_string(str):
    upper_let = ''.join(m for m in str if m.isupper())
    lower_let = ''.join(m for m in str if m.islower())
    return upper_let + lower_let