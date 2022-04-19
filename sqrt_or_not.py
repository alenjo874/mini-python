# Write a method, that will get an integer array as parameter and will process every number from this array.
# Return a new array with processing every number of the input-array like this:
# If the number has an integer square root, take this, otherwise square the number.

def square_or_square_root(arr):
    import math
    result = []
    for num in arr:
        if math.isqrt(num) * math.isqrt(num) == num:
            result.append(math.isqrt(num))
        else: 
            result.append(num * num)
    return result