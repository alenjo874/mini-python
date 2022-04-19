# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!

def better_than_average(class_points, your_points):
    
    total = sum(class_points) + your_points
    students = len(class_points) + 1
    avg = total / students
    
    if avg > your_points:
        return False
    else:
        return True