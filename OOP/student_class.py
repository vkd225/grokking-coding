class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.grade = grade #0-100
    self.age = age

  def get_grade(self):
    return self.grade

class Course:
  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students
    self.students = []
    self.is_active = False

  def add_student(self, student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      return True
    return False

  def get_avg_grade(self):
    grades = 0
    for student in self.students:
      grades += student.get_grade()

    return grades/len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)

course.add_student(s1)
course.add_student(s2)

course.add_student(s3) # would not go through since max_students = 2

print(course.students[0].name)

print(course.get_avg_grade())
