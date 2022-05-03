# Write a function that returns a string in which firstname is swapped with last name.

def name_shuffler(str):
    new_name = str.split(" ")
    return new_name[1] + " " + new_name[0]