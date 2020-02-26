class Department:
    class BudgetError(ValueError):
        pass

    def __init__(self, name, employees, budget):
        self.name = name
        self.employees = employees
        self.budget = budget

    def get_budget_plan(self):
        result = self.budget - sum(self.employees.values())
        if result < 0:
            raise self.BudgetError
        return result

    def get_average_salary(self):
        return round(
            sum(self.employees.values()) / len(self.employees),
            2
        )

    def merge_departments(self, *departments):
        names = []
        new_budget = 0
        new_employees = {}

        for department in departments:
            names.append(department.name)
            new_budget += department.budget
            new_employees.update(department.employees)
        new_name = ' - '.join(names)

        if new_budget < sum(new_employees.values()):
            raise self.BudgetError
        return Department(new_name, new_employees, new_budget)

    def __add__(self, other):
        return self.merge_departments(self, other)

    def __or__(self, other):
        plan_1 = self.budget - sum(self.employees.values())
        plan_2 = other.budget - sum(other.employees.values())
        if plan_1 < 0 or plan_2 < 0:
            raise self.BudgetError
        return self if plan_1 >= plan_2 else other
        
dep1 = Department("bsu", 1500, {'vlad': 1000, 'nik': 400})
dep2 = Department("qqq", 5555, {'ivan': 100, 'john': 140})
# print(dep1)  
# print(dep1.get_budget_plan())
# print(dep2.get_budget_plan())
dep3 = dep2 + dep1
print(dep3)
