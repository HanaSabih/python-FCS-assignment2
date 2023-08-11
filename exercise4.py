# Python has an inbuilt function called max() that returns the element with the maximum
# value.
# Create a function that does a very similar thing (without using the max() function). The
# function takes a list of numbers l as a parameter and returns the highest number in the list and
# its index.
# EX: if l = [5,6,3,2,7,2,0,1,6], the function should return “the highest value in the list is 7 at
# index 4”
# (BONUS: do the same but for the minimum)


#################################################################################


# O(n) =>  n = the length of the input list lst

def find_extreme(lst):
    if not lst:
        return "The list is empty."

    max_v = lst[0]
    max_idx = 0
    min_v = lst[0]
    min_idx = 0

    for i, num in enumerate(lst):
        if num > max_v:
            max_v = num
            max_idx = i
        if num < min_v:
            min_v = num
            min_idx = i

    max_res = f"The highest value in the list is {max_v} at index {max_idx}."
    min_res = f"The lowest value in the list is {min_v} at index {min_idx}."

    return max_res, min_res