import statistics
def enrollment_stats(universities):
    students, tuitions = [], []
    for university in universities:
        students.append(university[1])
        tuitions.append(university[2])
    return sum(students), sum(tuitions)

def a_mean(universities):
    students, tuitions = [], []
    for university in universities:
        students.append(university[1])
        tuitions.append(university[2])
    return statistics.mean(students), statistics.mean(tuitions)

def a_median(universities):
    students, tuitions = [], []
    for university in universities:
        students.append(university[1])
        tuitions.append(university[2])
    return statistics.median(students), statistics.median(tuitions)
    
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

all_students, all_tuitions = enrollment_stats(universities)
mean_students, mean_tuitions = a_mean(universities)
median_students, median_tuitions = a_median(universities)

print("******************************")
print(f"Total students: {all_students:,}")
print(f"Total tuition: $ {all_tuitions:,}\n")
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,}\n")
print(f"Tuition mean: $ {mean_tuitions:,.2f}")
print(f"Tuition median: $ {median_tuitions:,}")
print("******************************")
