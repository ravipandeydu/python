class Student:
    """
    Represents a student in the university, managing personal information,
    enrollments, and academic records like GPA and transcripts.
    """

    _total_students = 0
    _all_students = []

    def __init__(self, student_id, name, email, program):
        """
        Initializes a new Student.

        Args:
            student_id (str): Unique ID for the student.
            name (str): Student's name.
            email (str): Student's email.
            program (str): The student's academic program.
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.program = program
        self.enrollments = {}  # {course_id: enrollment_object}
        Student._total_students += 1
        Student._all_students.append(self)

    def enroll_in_course(self, course):
        """Enrolls the student in a course."""
        if course.is_full():
            course.add_to_waitlist(self)
            return f"Course {course.course_id} is full. Added to waitlist."

        enrollment = Enrollment(self, course)
        self.enrollments[course.course_id] = enrollment
        course.add_enrollment(enrollment)
        return f"Enrolled in {course.course_id}."

    def add_grade(self, course_id, grade):
        """Adds a grade for an enrolled course."""
        if course_id in self.enrollments:
            self.enrollments[course_id].set_grade(grade)
            return "Grade added."
        return "Student not enrolled in this course."

    def calculate_gpa(self):
        """Calculates the student's GPA."""
        total_points = 0
        total_credits = 0
        for enrollment in self.enrollments.values():
            if enrollment.grade is not None:
                # A simple GPA scale (e.g., 90-100: 4.0, 80-89: 3.0, etc.)
                if enrollment.grade >= 90:
                    grade_point = 4.0
                elif enrollment.grade >= 80:
                    grade_point = 3.0
                elif enrollment.grade >= 70:
                    grade_point = 2.0
                elif enrollment.grade >= 60:
                    grade_point = 1.0
                else:
                    grade_point = 0.0

                total_points += grade_point * enrollment.course.credits
                total_credits += enrollment.course.credits

        return total_points / total_credits if total_credits > 0 else 0.0

    def get_transcript(self):
        """Returns the student's academic transcript."""
        return {
            course_id: enrollment.grade
            for course_id, enrollment in self.enrollments.items()
        }

    def __str__(self):
        return f"Student: {self.name} ({self.student_id}), Program: {self.program}"

    @classmethod
    def get_total_students(cls):
        """Returns the total number of students."""
        return cls._total_students

    @classmethod
    def get_average_gpa(cls):
        """Calculates the average GPA across all students."""
        if not cls._all_students:
            return 0.0
        total_gpa = sum(student.calculate_gpa() for student in cls._all_students)
        return total_gpa / len(cls._all_students)

    @classmethod
    def get_top_students(cls, n=3):
        """Returns the top N students by GPA."""
        sorted_students = sorted(
            cls._all_students, key=lambda s: s.calculate_gpa(), reverse=True
        )
        return [(s.name, s.calculate_gpa()) for s in sorted_students[:n]]


class Course:
    """
    Represents a university course, managing enrollments, capacity,
    and a waitlist.
    """

    _total_enrollments = 0

    def __init__(self, course_id, name, instructor, credits, capacity):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
        self.credits = credits
        self.capacity = capacity
        self.enrollments = []
        self.waitlist = []

    def add_enrollment(self, enrollment):
        self.enrollments.append(enrollment)
        Course._total_enrollments += 1

    def get_enrollment_count(self):
        return len(self.enrollments)

    def get_available_spots(self):
        return self.capacity - self.get_enrollment_count()

    def is_full(self):
        return self.get_enrollment_count() >= self.capacity

    def add_to_waitlist(self, student):
        self.waitlist.append(student)

    def get_course_stats(self):
        """Calculates statistics for the course."""
        grades = [e.grade for e in self.enrollments if e.grade is not None]
        if not grades:
            return {"average": 0, "highest": 0, "lowest": 0}
        return {
            "average": sum(grades) / len(grades),
            "highest": max(grades),
            "lowest": min(grades),
        }

    def __str__(self):
        return f"Course: {self.name} ({self.course_id}), Instructor: {self.instructor}"

    @classmethod
    def get_total_enrollments(cls):
        """Returns the total number of enrollments across all courses."""
        return cls._total_enrollments


class Enrollment:
    """Links a student to a course and stores the grade."""

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None

    def set_grade(self, grade):
        self.grade = grade


# --- Test Cases ---

# Test Case 1: Creating courses with enrollment limits
math_course = Course("MATH101", "Calculus I", "Dr. Smith", 3, 30)
physics_course = Course("PHYS101", "Physics I", "Dr. Johnson", 4, 25)
cs_course = Course(
    "CS101", "Programming Basics", "Prof. Brown", 3, 2
)  # Small capacity for testing

print(f"Course: {math_course}")
print(f"Available spots in Math: {math_course.get_available_spots()}")
print("-" * 30)

# Test Case 2: Creating students with different programs
student1 = Student("S001", "Alice Wilson", "alice@university.edu", "Computer Science")
student2 = Student("S002", "Bob Davis", "bob@university.edu", "Mathematics")
student3 = Student("S003", "Carol Lee", "carol@university.edu", "Physics")

print(f"Student: {student1}")
print(f"Total students: {Student.get_total_students()}")
print("-" * 30)

# Test Case 3: Course enrollment
enrollment1 = student1.enroll_in_course(math_course)
enrollment2 = student1.enroll_in_course(cs_course)
enrollment3 = student2.enroll_in_course(math_course)

print(f"Alice's enrollment in Math: {enrollment1}")
print(f"Math course enrollment count: {math_course.get_enrollment_count()}")
print("-" * 30)

# Test Case 4: Adding grades and calculating GPA
student1.add_grade("MATH101", 85.5)
student1.add_grade("CS101", 92.0)
student2.add_grade("MATH101", 78.3)

print(f"Alice's GPA: {student1.calculate_gpa():.2f}")
print(f"Alice's transcript: {student1.get_transcript()}")
print("-" * 30)

# Test Case 5: Course statistics
math_course_stats = math_course.get_course_stats()
print(f"Math course statistics: {math_course_stats}")
print("-" * 30)

# Test Case 6: University-wide analytics using class methods
total_enrollments = Course.get_total_enrollments()
print(f"Total enrollments across all courses: {total_enrollments}")

average_gpa = Student.get_average_gpa()
print(f"University average GPA: {average_gpa:.2f}")

top_students = Student.get_top_students(2)
print(f"Top 2 students: {top_students}")
print("-" * 30)

# Test Case 7: Enrollment limits and waitlist
# Try to enroll more students than course capacity in CS
student2.enroll_in_course(cs_course)  # Fills the course
result = student3.enroll_in_course(cs_course)  # Should go to waitlist
print(f"Course full status: {cs_course.is_full()}")
print(f"Waitlist size: {len(cs_course.waitlist)}")
print(f"Carol's enrollment attempt: {result}")
