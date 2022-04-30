# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_char(s):
    result = list(s)

    result.pop(0)
    
    result.pop(len(result) - 1)
   
    return "".join(result)