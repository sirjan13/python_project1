grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#Prints grades as in list
def print_grades(grades):
    for grade in grades:
        print grade

#return sum of grades
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

#finds mean or average of list
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

#finds variance acc to formula sumof((mean-score)^2) for score in list grades
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= len(scores)
    return variance


def grades_std_deviation(variance):
    return variance ** 0.5


print 'variance = ',grades_variance(grades)

print 'standard deviation = ',grades_std_deviation(grades_variance(grades))


