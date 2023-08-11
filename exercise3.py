# Create a function that takes two strings s1 and s2 as parameters and returns True if s1 is a
# reordering of the characters in s2.
# EX: if s1=”abcde” and s2=”edacb” , the function returns True. If s1=”aabc” and s2=”edabc”,
# the
# function returns False.

#####################################################################################

# O(n log n) =>  'n' = the length of the longer input string between str1 and str2

def reordering(str1, str2):
    s1 = sorted(str1)
    s2 = sorted(str2)
    return s1 == s2