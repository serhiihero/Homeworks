# Create a class describing any company. For example, Toshiba or Apple

class Employee:

    def __init__(self, employee_name: str, employee_sex: str, employee_age: int, employee_education: str, employment: str):
        self.__employee_name = employee_name
        self.__employee_sex = employee_sex
        self.__employee_age = employee_age
        self.__employee_education = employee_education
        self.__employment = employment

    @property
    def name(self):
        if isinstance(self.__employee_name, str) and len(self.__employee_name) <= 20:
            return self.__employee_name
        else:
            raise TypeError('No longer than 20 letters expected for the employee name.')

    @name.setter
    def name(self, new_employee_name):
        if isinstance(new_employee_name, str) and len(new_employee_name) <= 20:
            self.__employee_name = new_employee_name
        else:
            raise TypeError('No longer than 20 letters expected for the employee name.')

    @property
    def sex(self):
        if isinstance(self.__employee_sex, str) and self.__employee_sex.lower() in ["male", "female"]:
            return self.__employee_sex
        else:
            raise SyntaxError('Sex must be "male" or "female".')

    @sex.setter
    def sex(self, employee_sex_change):
        if isinstance(employee_sex_change, str) and employee_sex_change.lower() in ["male", "female"]:
            self.__employee_sex = employee_sex_change
        else:
            raise SyntaxError('Sex must be "male" or "female".')

    @property
    def age(self):
        if isinstance(self.__employee_age, int) and 18 <= self.__employee_age <= 60:
            return self.__employee_age
        else:
            raise TypeError('Only over 18 and no over 60 are allowed.')

    @age.setter
    def age(self, employee_age_change):
        if isinstance(employee_age_change, int) and 18 <= employee_age_change <= 60:
            self.__employee_age = employee_age_change
        else:
            raise TypeError('Only over 18 and no over 60 are allowed.')

    @property
    def education(self):
        if isinstance(self.__employee_education, str) and len(self.__employee_education) <= 30:
            return self.__employee_education
        else:
            raise TypeError('Education must be a string with no more than 30 characters.')

    @education.setter
    def education(self, employee_education_change):
        if isinstance(employee_education_change, str) and len(employee_education_change) <= 30:
            self.__employee_education = employee_education_change
        else:
            raise TypeError('Education must be a string with no more than 30 characters.')

    @property
    def employment(self):
        if isinstance(self.__employment, str) and self.__employment.lower() in ["full-time", "part-time"]:
            return self.__employment
        else:
            raise TypeError('Employment must be "full-time" or "part-time".')

    @employment.setter
    def employment(self, employment_change):
        if isinstance(employment_change, str) and employment_change.lower() in ["full-time", "part-time"]:
            self.__employment = employment_change
        else:
            raise TypeError('Employment must be "full-time" or "part-time".')


if __name__ == '__main__':
    result = Employee('Adel', 'female', 25, 'High', 'full-time')
