class Student:
    def __init__(self, age , height , weight):
        self.age = age
        self.height = height
        self.weight = weight

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self):
        self.students.append(Student)
    
    def calculate_average(self):
        total_age = 0
        total_height = 0
        total_weight = 0

        for student in self.students:
            total_age += student.age
            total_height += student.height
            total_weight += student.weight

        average_age = total_age / len(self.students)
        average_height = total_height / len(self.students)
        average_weight = total_weight / len(self.students)

        return average_age, average_height , average_weight

def compare_schools(f,g):
    average_age_a, average_height_a , average_weight_a = school_a.calculate_average()
    average_age_b, average_height_b , average_weight_b = school_b.calculate_average()
    print(average_age_a)
    print(average_height_a)
    print(average_weight_a)
    print(average_age_b)
    print(average_height_b)
    print(average_weight_b)

    if average_height_a > average_height_b:
        print(school_a.name)
    elif average_height_b > average_height_a:
        print(school_b.name)
    else:
        if average_weight_a < average_weight_b:
            print(school_a.name)
        elif average_weight_a > average_weight_b:
            print(school_b.name)
        else:
            print('Same')


def input_student_data(n):
    students = []
    ages = list(map(float,input().split()))
    height = list(map(float,input().split()))
    weight = list(map(float,input().split()))

    for i in range(n):
        students.append(Student(ages[i],height[i],weight[i]))
    return students

n_a = int(input())
students_a = input_student_data(n_a)
n_b = int(input())
students_b = input_student_data(n_b)

school_a = School('A')
school_a.students = students_a
school_b = School('B')
school_b.students = students_b

compare_schools(school_a,school_b)
