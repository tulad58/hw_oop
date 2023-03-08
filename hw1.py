class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f"Имя: {self.name}\n"
              f"Фамилия: {self.surname}\n"
              f"Средняя оценка за оекцию: {self.avarage_grade()}\n"
              f"Курсы в процессе изучения: {self.courses_in_progress}\n"
              f"Завершенные курсы: {self.finished_courses}")

    def avarage_grade(self):
        return sum(self.grades.values()) / len(self.grades)

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.avarage_grade() < other.avarage_grade():
                return f"{other.name}"
            else:
                return f"{self.name}"



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за оекцию: {self.avarage_grade()}")

    def avarage_grade(self):
        return sum(self.grades.values()) / len(self.grades)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.avarage_grade() < other.avarage_grade():
                return f"{other.name}"
            else:
                return f"{self.name}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f"Имя: {self.name}\nФамилия: {self.surname}")


