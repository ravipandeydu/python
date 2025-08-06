from collections import defaultdict


class GradeManager:
    """
    Manages student grades using defaultdict for efficient data organization.
    """

    def __init__(self):
        """
        Initializes the GradeManager with appropriate defaultdict structures
        to avoid key existence checks.
        """
        # Stores grades by student: {'student_name': [('subject', grade), ...]}
        self.student_grades = defaultdict(list)
        # Stores grades by subject: {'subject': [('student_name', grade), ...]}
        self.subject_grades = defaultdict(list)

    def add_grade(self, student_name, subject, grade):
        """
        Adds a grade for a student in a specific subject.

        Args:
            student_name (str): Name of the student.
            subject (str): Subject name.
            grade (float): Grade value (0-100).
        """
        self.student_grades[student_name].append((subject, grade))
        self.subject_grades[subject].append((student_name, grade))

    def get_student_average(self, student_name):
        """
        Calculates the average grade for a student across all subjects.

        Args:
            student_name (str): Name of the student.

        Returns:
            float: Average grade or 0 if the student is not found.
        """
        grades = self.student_grades[student_name]
        if not grades:
            return 0
        total = sum(grade for subject, grade in grades)
        return total / len(grades)

    def get_subject_statistics(self, subject):
        """
        Gets statistics for a specific subject across all students.

        Args:
            subject (str): Subject name.

        Returns:
            dict: Contains 'average', 'highest', 'lowest', 'student_count'.
        """
        grades = self.subject_grades[subject]
        if not grades:
            return {"average": 0, "highest": 0, "lowest": 0, "student_count": 0}

        student_grades = [grade for student, grade in grades]
        student_count = len(student_grades)
        total_grade = sum(student_grades)

        return {
            "average": total_grade / student_count,
            "highest": max(student_grades),
            "lowest": min(student_grades),
            "student_count": student_count,
        }

    def get_top_students(self, n=3):
        """
        Gets top N students based on their overall average.

        Args:
            n (int): Number of top students to return.

        Returns:
            list: List of tuples (student_name, average_grade).
        """
        averages = []
        for student in self.student_grades:
            avg = self.get_student_average(student)
            averages.append((student, avg))

        # Sort by average grade in descending order
        averages.sort(key=lambda x: x[1], reverse=True)
        return averages[:n]

    def get_failing_students(self, passing_grade=60):
        """
        Gets students who are failing (average below passing grade).

        Args:
            passing_grade (float): Minimum grade to pass.

        Returns:
            list: List of tuples (student_name, average_grade).
        """
        failing_students = []
        for student in self.student_grades:
            avg = self.get_student_average(student)
            if avg < passing_grade:
                failing_students.append((student, avg))
        return failing_students


# Test your implementation
manager = GradeManager()

# Add sample grades
grades_data = [
    ("Alice", "Math", 85),
    ("Alice", "Science", 92),
    ("Alice", "English", 78),
    ("Bob", "Math", 75),
    ("Bob", "Science", 68),
    ("Bob", "English", 82),
    ("Charlie", "Math", 90),
    ("Charlie", "Science", 88),
    ("Charlie", "History", 91),
    ("Diana", "Math", 55),
    ("Diana", "Science", 62),
    ("Diana", "English", 70),
    ("Eve", "Math", 88),
    ("Eve", "Science", 94),
    ("Eve", "English", 86),
    ("Eve", "History", 89),
]

for student, subject, grade in grades_data:
    manager.add_grade(student, subject, grade)

# Test all methods
print(f"Alice's average: {manager.get_student_average('Alice')}")
print(f"Math statistics: {manager.get_subject_statistics('Math')}")
print(f"Top 3 students: {manager.get_top_students(3)}")
print(f"Failing students (passing grade 75): {manager.get_failing_students(75)}")
