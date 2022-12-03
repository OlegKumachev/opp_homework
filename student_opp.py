from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.score = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course \
                in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mid_rate(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        res = f'Имя:{self.name} \nФамилия: {self.surname} \
        \nКурсы в процессе изучения: {", " .join(self.courses_in_progress)}'
        f' \nЗавершенные курсы: {"" .join(self.finished_courses)}'
        f'\nСредняя оценка за домашнее задание {self.mid_rate()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить')
            return
        return self.mid_rate() > other.mid_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in \
         self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя:{self.name} \nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    grades = {}

    def mid_rate(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        res = f'Имя:{self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.mid_rate()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить')
            return
        return self.mid_rate() > other.mid_rate()


best_student = Student('Jimi', 'Hendrix', 'male')
best_student.courses_in_progress += ['Java']
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

cool_student = Student('Steven', 'Tyler', 'male')
cool_student.courses_in_progress += ['Java']
cool_student.courses_in_progress += ['Python']
cool_student.finished_courses += ['Введение в программирование']

best_lecturer = Lecturer('Chuck', 'Berry')
cool_lecturer = Lecturer('Elvis', 'Presley')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']

best_reviewer = Reviewer('Axl', 'Rose')
best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Java']

cool_reviewer = Reviewer('Serj', 'Tankian')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']

best_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Java', 8)

best_reviewer.rate_hw(cool_student, 'Python', 10)
cool_reviewer.rate_hw(cool_student, 'Java', 8)

best_student.rate_lec(cool_lecturer, 'Python', 8)
cool_student.rate_lec(cool_lecturer, 'Python', 9)
best_student.rate_lec(best_lecturer, 'Java', 8)

best_student.rate_lec(best_lecturer, 'Python', 10)
student_list = [best_student, cool_student]
lecturer_list = [best_lecturer, cool_lecturer]


def stud_mid_rate(course, catalogue):
    mid = []
    for person in catalogue:
        for key, val in person.grades.items():
            if key == course:
                mid += val
    return f'Cредняя оценка по {course} {mean(mid)}'


def lect_mid_rate(course, catalogue):
    mid = []
    for person in catalogue:
        for key, val in person.grades.items():
            if key == course:
                mid += val
    return f'Cредняя оценка по {course} {mean(mid)}'


print(best_reviewer)
print()
print(cool_reviewer)
print()
print(best_lecturer)
print()
print(cool_lecturer)
print()
print(best_student)
print()
print(cool_student)

print('=' * 50)

print(stud_mid_rate('Java', student_list))
print(lect_mid_rate('Python', lecturer_list))

