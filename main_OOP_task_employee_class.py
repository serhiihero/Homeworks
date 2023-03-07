# Create a class with a description of the worker. Any worker. employees.
# I will evaluate the completeness of the described class and will withdraw points for everything unnecessary.
# I want to see clean code. I expect to see clean code with annotations.
# So far, no first-class connections with the second. In all methods,
# I expect to see docstrings with a sane description.
import datetime


class Employee:
    MIN_EMPLOYEE_NAME_LENGTH = 1
    MAX_EMPLOYEE_NAME_LENGTH = 20
    MIN_EMPLOYEE_SEX_LENGTH = 1
    MAX_EMPLOYEE_SEX_LENGTH = 20
    MIN_EMPLOYEE_AGE = 18
    MAX_EMPLOYEE_AGE = 60
    MIN_EMPLOYEE_EDUCATION_LENGTH = 1
    MAX_EMPLOYEE_EDUCATION_LENGTH = 30
    MIN_EMPLOYMENT_LENGTH = 1
    MAX_EMPLOYMENT_LENGTH = 15

    def __init__(self, employee_name: str = None, employee_sex: str = None, employee_age: int = None,
                 employee_education: str = None, employment: str = None):
        self.__employee_name = employee_name
        self.__employee_sex = employee_sex
        self.__employee_age = employee_age
        self.__employee_education = employee_education
        self.__employment = employment

    @property
    def employee_name(self):
        return self.__employee_name

    @employee_name.setter
    def employee_name(self, new_employee_name):
        if self.is_valid_employee_name(new_employee_name):
            self.__employee_name = new_employee_name
        else:
            raise TypeError('No longer than 20 letters expected for the employee name.')

    @staticmethod
    def is_valid_employee_name(employee_name):
        return isinstance(employee_name,
                          str) and Employee.MIN_EMPLOYEE_NAME_LENGTH <= len(
            employee_name) <= Employee.MAX_EMPLOYEE_NAME_LENGTH

    @property
    def employee_sex(self):
        return self.__employee_sex

    @employee_sex.setter
    def employee_sex(self, employee_sex_change):
        if self.is_valid_employee_sex(employee_sex_change):
            self.__employee_sex = employee_sex_change
        else:
            raise TypeError('Sex must be "male" or "female".')

    @staticmethod
    def is_valid_employee_sex(employee_sex):
        return isinstance(employee_sex,
                          str) and Employee.MIN_EMPLOYEE_SEX_LENGTH <= len(
            employee_sex) <= Employee.MAX_EMPLOYEE_SEX_LENGTH and employee_sex.lower() in ["male", "female"]

    @property
    def employee_age(self):
        return self.__employee_age

    @employee_age.setter
    def employee_age(self, employee_age_change):
        if self.is_valid_employee_age(employee_age_change):
            self.__employee_age = employee_age_change
        else:
            raise TypeError('Only over 18 and no over 60 are allowed.')

    @staticmethod
    def is_valid_employee_age(employee_age):
        return isinstance(employee_age, int) and Employee.MIN_EMPLOYEE_AGE <= employee_age <= Employee.MAX_EMPLOYEE_AGE

    @property
    def employee_education(self):
        return self.__employee_education

    @employee_education.setter
    def employee_education(self, employee_education_change):
        if self.is_valid_employee_education(employee_education_change):
            self.__employee_education = employee_education_change
        else:
            raise TypeError('Education must be a string with no more than 30 characters.')

    @staticmethod
    def is_valid_employee_education(employee_education):
        return isinstance(employee_education,
                          str) and Employee.MIN_EMPLOYEE_EDUCATION_LENGTH <= len(
            employee_education) <= Employee.MAX_EMPLOYEE_EDUCATION_LENGTH

    @property
    def employment(self):
        return self.__employment

    @employment.setter
    def employment(self, employment_change):
        if self.is_valid_employment(employment_change):
            self.__employment = employment_change
        else:
            raise TypeError('Employment must be "full-time" or "part-time".')

    @staticmethod
    def is_valid_employment(employment):
        return isinstance(employment,
                          str) and Employee.MIN_EMPLOYMENT_LENGTH <= len(
            employment) <= Employee.MAX_EMPLOYMENT_LENGTH and employment.lower() in ["full-time", "part-time"]

    @staticmethod
    def calculate_age_of_employee(employee_age):
        years_old = datetime.datetime.now().year - employee_age
        return years_old

    def short_user_introduction(self):
        return f"{self.employee_name} has {self.employee_education} degree and pretend to work {self.employment}"

    @classmethod
    def add_new_employee(cls, employee_name, employment):
        return cls(employee_name, employment)


if __name__ == '__main__':
    Employee('Adel', 'female', 25, 'High', 'full-time')
