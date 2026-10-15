class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}: {self.calculate_salary()}'


class Manager(Employee):
    def __init__(self, name, base_salary, team_size, bonus_per_member=5000):
        super().__init__(name, base_salary)
        self.team_size = team_size
        self.bonus_per_member = bonus_per_member

    def calculate_salary(self):
        return super().calculate_salary() + self.team_size * self.bonus_per_member


class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours, hourly_rate=1000):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return super().calculate_salary() + self.overtime_hours * self.hourly_rate


if __name__ == '__main__':
    staff = [
        Employee('Иван', 50000),
        Manager('Ольга', 100000, team_size=5),
        Developer('Пётр', 120000, overtime_hours=10),
    ]
    for e in staff:
        print(e)
