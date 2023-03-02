# Create a class describing any company. For example, Toshiba or Apple

class Toshiba:
    MIN_COMPANY_NAME_LENGTH = 1
    MAX_COMPANY_NAME_LENGTH = 50
    MIN_FOUNDED_YEAR = 1882
    MAX_FOUNDED_YEAR = 2023
    MIN_FOUNDER_NAME_LENGTH = 1
    MAX_FOUNDER_NAME_LENGTH = 20
    MIN_EMPLOYEES_QUANTITY = 0
    MIN_REVENUE_QUANTITY = 0

    def __init__(self, company_name: str = None, founded_year: int = None, founder_name: str = None,
                 employees: int = None, revenue: int = None):
        self.__company_name = company_name
        self.__founded_year = founded_year
        self.__founder_name = founder_name
        self.__employees = employees
        self.__revenue = revenue

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, new_company_name):
        if self.is_valid_company_name(new_company_name):
            self.__company_name = new_company_name
        else:
            raise TypeError('Company name must be a string with no more than 50 characters.')

    @staticmethod
    def is_valid_company_name(company_name):
        return isinstance(company_name, str) and Toshiba.MIN_COMPANY_NAME_LENGTH <= len(
            company_name) <= Toshiba.MAX_COMPANY_NAME_LENGTH

    @property
    def founded_year(self):
        return self.__founded_year

    @founded_year.setter
    def founded_year(self, new_founded_year):
        if self.is_valid_founded_year(new_founded_year):
            self.__founded_year = new_founded_year
        else:
            raise TypeError('Company year can not be earlier than date of creation or current year.')

    @staticmethod
    def is_valid_founded_year(founded_year):
        return isinstance(founded_year, int) and Toshiba.MIN_FOUNDED_YEAR <= founded_year <= Toshiba.MAX_FOUNDED_YEAR

    @property
    def founder_name(self):
        return self.__founder_name

    @founder_name.setter
    def founder_name(self, new_founder_name):
        if self.is_valid_founder_name(new_founder_name):
            self.__founder_name = new_founder_name
        else:
            raise TypeError('No longer than 20 letters expected for the founder name.')

    @staticmethod
    def is_valid_founder_name(founder_name):
        return isinstance(founder_name,
                          str) and Toshiba.MIN_FOUNDER_NAME_LENGTH <= len(
            founder_name) <= Toshiba.MAX_FOUNDER_NAME_LENGTH

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, new_quantity_of_employees):
        if self.is_valid_employees(new_quantity_of_employees):
            self.__employees = new_quantity_of_employees
        else:
            raise TypeError('Only whole numbers which are starts from 0 are expected for this field.')

    @staticmethod
    def is_valid_employees(employees):
        return isinstance(employees, int) and Toshiba.MIN_EMPLOYEES_QUANTITY <= employees

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, raise_of_revenue):
        if self.is_valid_revenue_quantity(raise_of_revenue):
            self.__revenue = raise_of_revenue
        else:
            raise TypeError('Only whole or fractional numbers which are starts from 0 are expected for this field.')

    @staticmethod
    def is_valid_revenue_quantity(revenue):
        return isinstance(revenue, int | float) and Toshiba.MIN_REVENUE_QUANTITY <= revenue


if __name__ == '__main__':
    Toshiba('Toshiba Corporation', 1882, 'Tanaka Hisashige', 100, 15000)
