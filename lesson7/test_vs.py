class Department:
    class BudgetError(ValueError):
        pass
    lst = []
    def __init__(self, name, budget, employees={}):
        self.name = name
        self.employees = employees
        self.budget = budget

    def __str__(self):
        lst = [i for i in self.employees.keys()]
        return f'Name of department:{self.name}(workers: {len(lst)}  - average selary: {self.get_average_selary()}), budget: {self.budget}'

    def __repr__(self): 
        return str(self)

    def get_average_selary(self):
        lst = [i for i in self.employees.values()]
        return round(sum(lst) / len(lst), 2) if sum(lst) else None

    def get_budget_plan(self):
        sal = [i for i in self.employees.values()]
        return (self.budget - sum(sal))

    # def merge_departments(*args):
    #     return sum(args)

    def __add__(self, other):
        return Department(
            f'{self.name} - {other.name}',
            self.budget + other.budget,
            {**self.employees,**other.employees}
        )    

    def __or__(self, other):
        return self if self.get_budget_plan > other.get_budget_plan else other
         
        
dep1 = Department("bsu", 1500, {'vlad': 1000, 'nik': 400})
dep2 = Department("qqq", 5555, {'ivan': 100, 'john': 140})
# print(dep1)  
# print(dep1.get_budget_plan())
# print(dep2.get_budget_plan())
dep3 = dep2 + dep1
print(dep3)
