import re
from datetime import date, timedelta


class Employee:
    """
    Manages employee data and company-wide statistics for a multinational company.

    This class handles individual employee records, tracks company-wide metrics
    like total employees and department counts, and provides utility methods
    for calculations like payroll and performance.
    """

    # Class variables (shared across all instances)
    company_name: str = "GlobalTech Solutions"
    total_employees: int = 0
    departments: dict[str, int] = {
        "Engineering": 0,
        "Sales": 0,
        "HR": 0,
        "Marketing": 0,
    }
    tax_rates: dict[str, float] = {"USA": 0.22, "India": 0.18, "UK": 0.25}
    next_employee_id_counter: int = 1

    def __init__(
        self, name: str, department: str, base_salary: int, country: str, email: str
    ):
        """Initializes an Employee instance and updates class-level statistics."""
        # Instance variables
        self.name = name
        if not Employee.is_valid_department(department):
            raise ValueError(f"Department '{department}' is not a valid department.")
        self.department = department
        self.base_salary = base_salary
        self.country = country
        if not Employee.validate_email(email):
            raise ValueError(f"Invalid email format: {email}")
        self.email = email
        self.hire_date: date = date.today()
        self.performance_ratings: list[float] = []

        # Assign a unique ID and update class-level trackers
        self.employee_id = Employee.generate_employee_id()
        Employee.total_employees += 1
        Employee.departments[self.department] += 1

    # --- Static Methods ---
    @staticmethod
    def generate_employee_id() -> str:
        """Creates a unique employee ID in the format 'EMP-YYYY-XXXX'."""
        year = date.today().year
        emp_num = Employee.next_employee_id_counter
        Employee.next_employee_id_counter += 1
        return f"EMP-{year}-{emp_num:04d}"

    @staticmethod
    def validate_email(email: str) -> bool:
        """Checks for a proper email format (e.g., user@domain.com)."""
        # A simple regex to check for a basic email structure.
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    @staticmethod
    def calculate_tax(salary: float, country: str) -> float:
        """Calculates tax based on the employee's country."""
        rate = Employee.tax_rates.get(country, 0)  # Default to 0 if country not found
        return salary * rate

    @staticmethod
    def is_valid_department(dept: str) -> bool:
        """Checks if a department is in the approved list."""
        return dept in Employee.departments

    # --- Class Methods ---
    @classmethod
    def from_csv_data(cls, csv_line: str):
        """Creates an Employee instance from a CSV formatted string."""
        name, dept, salary_str, country, email = csv_line.strip().split(",")
        return cls(name, dept, int(salary_str), country, email)

    @classmethod
    def get_department_stats(cls) -> dict:
        """Returns a dictionary with detailed statistics for each department."""
        stats = {}
        for dept, count in cls.departments.items():
            stats[dept] = {"count": count}
        return stats

    @classmethod
    def set_tax_rate(cls, country: str, rate: float):
        """Updates the tax rate for a specific country."""
        if 0 <= rate <= 1:
            cls.tax_rates[country] = rate
        else:
            raise ValueError("Tax rate must be between 0 and 1.")

    @classmethod
    def hire_bulk_employees(cls, employee_csv_list: list[str]) -> list["Employee"]:
        """Hires multiple employees from a list of CSV strings."""
        return [cls.from_csv_data(emp_data) for emp_data in employee_csv_list]

    # --- Instance Methods ---
    def add_performance_rating(self, rating: float):
        """Adds a performance rating (1-5 scale) to the employee's record."""
        if 1 <= rating <= 5:
            self.performance_ratings.append(rating)
        else:
            raise ValueError("Rating must be between 1 and 5.")

    def get_average_performance(self) -> float:
        """Calculates the employee's average performance rating."""
        if not self.performance_ratings:
            return 0.0
        return sum(self.performance_ratings) / len(self.performance_ratings)

    def calculate_net_salary(self) -> float:
        """Calculates the net salary after tax deductions."""
        tax_amount = Employee.calculate_tax(self.base_salary, self.country)
        return self.base_salary - tax_amount

    def get_years_of_service(self) -> float:
        """Calculates the total years of service from the hire date."""
        return (date.today() - self.hire_date).days / 365.25

    def is_eligible_for_bonus(self) -> bool:
        """Checks if the employee is eligible for a bonus."""
        return self.get_average_performance() > 3.5 and self.get_years_of_service() > 1

    def __repr__(self) -> str:
        """Provides a developer-friendly representation of the Employee object."""
        return f"Employee(id='{self.employee_id}', name='{self.name}', dept='{self.department}')"


### **Verification Against Test Cases**

# Here is the code executing the test cases from your image to verify its correctness.

# Test Case 1: Class setup and basic functionality
print("--- Running Test Case 1 ---")
Employee.company_name = "GlobalTech Solutions"
Employee.tax_rates = {"USA": 0.22, "India": 0.18, "UK": 0.25}
Employee.departments = {"Engineering": 0, "Sales": 0, "HR": 0, "Marketing": 0}

emp1 = Employee("John Smith", "Engineering", 85000, "USA", "john.smith@globaltech.com")
current_year = date.today().year
assert emp1.employee_id.startswith(f"EMP-{current_year}-")
assert Employee.total_employees == 1
assert Employee.departments["Engineering"] == 1
print("✅ Test Case 1 Passed")

# Test Case 2: Static method validations
print("\n--- Running Test Case 2 ---")
assert Employee.validate_email("test@company.com") == True
assert Employee.validate_email("invalid.email") == False
assert Employee.is_valid_department("Engineering") == True
assert Employee.is_valid_department("InvalidDept") == False
assert abs(Employee.calculate_tax(100000, "USA") - 22000) < 0.01
print("✅ Test Case 2 Passed")

# Test Case 3: Class methods and bulk operations
print("\n--- Running Test Case 3 ---")
emp2 = Employee.from_csv_data("Sarah Johnson,Sales,75000,UK,sarah.j@globaltech.com")
assert emp2.name == "Sarah Johnson"
assert emp2.department == "Sales"
assert Employee.departments["Sales"] == 1

bulk_data = [
    "Mike Wilson,Marketing,65000,India,mike.w@globaltech.com",
    "Lisa Chen,HR,70000,USA,lisa.chen@globaltech.com",
]
Employee.hire_bulk_employees(bulk_data)
assert Employee.total_employees == 4
print("✅ Test Case 3 Passed")

# Test Case 4: Performance and bonus calculations
print("\n--- Running Test Case 4 ---")
stats = Employee.get_department_stats()
assert stats["Engineering"]["count"] == 1
assert stats["Sales"]["count"] == 1

emp1.add_performance_rating(4.2)
emp1.add_performance_rating(3.8)
emp1.add_performance_rating(4.5)
assert abs(emp1.get_average_performance() - 4.166) < 0.01

# Simulate employee with 2 years of service for testing
emp1.hire_date = date.today() - timedelta(days=800)
assert emp1.get_years_of_service() > 2
assert emp1.is_eligible_for_bonus() == True
print("✅ Test Case 4 Passed")

# Test Case 5: Salary calculations
print("\n--- Running Test Case 5 ---")
net_salary = emp1.calculate_net_salary()
expected_net = 85000 - (85000 * 0.22)
assert abs(net_salary - expected_net) < 0.01
print("✅ Test Case 5 Passed")
