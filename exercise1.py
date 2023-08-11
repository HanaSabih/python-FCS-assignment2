# Create a function that takes a string s and an integer i as parameters and returns a string that
# has in it s reversed and concatenated i times.
# EX: if s is “hello” and i is 2, the function returns “olleholleh”. If i is 0, the function returns an
# empty string.

##############################################################################



# O(m * n) =>  m = the length of the input string and n = the number of times the reversed string is repeated


def reverse_string(str , n):
    return str[::-1]*n


