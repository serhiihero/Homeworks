# Create a class describing any company. For example, Toshiba or Apple

class Toshiba:

    def __init__(self, company_name, founded_year, founder_name, employees, revenue):
        self.__company_name = company_name
        self.__founded_year = founded_year
        self.__founder_name = founder_name
        self.__employees = employees
        self.__revenue = revenue

    @property
    def company_name(self):
        if isinstance(self.__company_name, str) and len(self.__company_name) <= 50:
            return self.__company_name
        else:
            raise TypeError('Company name must be a string with no more than 50 characters.')

    @company_name.setter
    def company_name(self, new_company_name):
        if isinstance(new_company_name, str) and len(new_company_name) <= 50:
            self.__company_name = new_company_name
        else:
            raise TypeError('Company name must be a string with no more than 50 characters.')

    @property
    def founded_year(self):
        if isinstance(self.__founded_year, int) and 1882 <= self.__founded_year <= 2023:
            return self.__founded_year
        else:
            raise SyntaxError('Company year can not be earlier than date of creation or current year.')

    @founded_year.setter
    def founded_year(self, new_founded_year):
        if isinstance(new_founded_year, int) and new_founded_year >= 1882:
            self.__founded_year = new_founded_year
        else:
            raise SyntaxError('Company year can not be earlier than date of creation or current year.')

    @property
    def founder_name(self):
        if isinstance(self.__founder_name, str) and len(self.__founder_name) <= 20:
            return self.__founder_name
        else:
            raise TypeError('No longer than 20 letters expected for the founder name.')

    @founder_name.setter
    def founder_name(self, new_founder_name):
        if isinstance(new_founder_name, str) and len(new_founder_name) <= 20:
            self.__founder_name = new_founder_name
        else:
            raise TypeError('No longer than 20 letters expected for the founder name.')

    @property
    def employees(self):
        if isinstance(self.__employees, int):
            return self.__employees
        else:
            raise TypeError('Only whole numbers are expected for this field.')

    @employees.setter
    def employees(self, new_quantity_of_employees):
        if isinstance(new_quantity_of_employees, int):
            self.__employees = new_quantity_of_employees
        else:
            raise TypeError('Only whole numbers are expected for this field.')

    @property
    def revenue(self):
        if isinstance(self.__revenue, int | float):
            return self.__revenue
        else:
            raise TypeError('Only whole or fractional numbers are expected for this field.')

    @revenue.setter
    def revenue(self, raise_of_revenue):
        if isinstance(raise_of_revenue, int | float):
            self.__revenue = raise_of_revenue
        else:
            raise TypeError('Only whole or fractional numbers are expected for this field.')


if __name__ == '__main__':
    result = Toshiba('Toshiba Corporation', 1882, 'Tanaka Hisashige', 100, 15000)
