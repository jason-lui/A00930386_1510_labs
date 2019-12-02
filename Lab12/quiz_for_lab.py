"""Brian Duong, Jason Lui"""


class Student:

    students = "A00000000"

    def __init__(self, first_name, last_name, list_of_courses, middle_name=""):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_num = Student.students
        self.__list_of_courses = list_of_courses
        self.__middle_name = middle_name

        count = 100000000 + int(Student.students[1:]) + 1
        Student.students = "A" + str(count)[1:]

    def get_gpa(self):
        avg = 0
        for v in self.__list_of_courses.values():
            avg += v
        avg /= len(self.__list_of_courses)
        return round(avg, 2)

    def get_student_information(self):
        name = " ".join([self.__first_name, self.__middle_name, self.__last_name]) if self.__middle_name else \
            " ".join([self.__first_name, self.__last_name])

        return f"Name: {name.title()}, Student Number: {self.__student_num}, " \
               f"Number of Courses: {len(self.__list_of_courses)}, GPA: {self.get_gpa()}."

    def change_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def add_course(self, new_class_name, class_grade):
        self.__list_of_courses[new_class_name] = class_grade


def main():
    nicole = Student("nicole", "brooks", {}, "paige")
    nicole.add_course("COMP 1510", 95)
    nicole.add_course("COMP 1113", 87)
    nicole.add_course("COMP 1536", 84)

    print(nicole.get_student_information())
    nicole.change_last_name("wang")
    print(nicole.get_student_information())

    cornelius = Student("cornelius", "smith", {})
    cornelius.add_course("COMM 1116", 45)
    cornelius.add_course("COMP 1930", 65)
    cornelius.add_course("COMP 1712", 75)

    print(cornelius.get_student_information())
    
    harold = Student("harold", "finch", {})
    harold.add_course("COMP 1510", 37)
    harold.add_course("COMP 1712", 40)
    harold.add_course("COMM 1116", 0)

    print(harold.get_student_information())


if __name__ == "__main__":
    main()
