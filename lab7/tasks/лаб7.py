class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f'Name: {self.name}, ID: {self.id}'


class Manager(Employee):
    def __init__(self, name="", id="", department=""):
        super().__init__(name, id)
        self.department = department

    def manage_project(self):
        return f"{self.name} is managing a project in the {self.department} department."


class Technician(Employee):
    def __init__(self, name="", id="", specialization=""):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} is performing maintenance in {self.specialization}."


class TechManager(Technician, Manager):
    def __init__(self, name, id, specialization, department):
        super().__init__(name, id, specialization)
        super().__init__(name, id, department)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_team_info(self):
        team_info = f"Team Info for {self.name}:\n"
        for employee in self.employees:
            team_info += employee.get_info() + "\n"
        return team_info

    def manage_project(self):
        return super().manage_project()

    def perform_maintenance(self):
        return super().perform_maintenance()

tech_manager = TechManager("John Doe", "E1234", "IT", "Network Administration")
manager = Manager("Jane Smith", "E5678", "Marketing")
technician = Technician("Bob Johnson", "E9012", "Hardware")
employee = Employee("Alice Brown", "E1111")

tech_manager.add_employee(manager)
tech_manager.add_employee(technician)
tech_manager.add_employee(employee)

print(tech_manager.get_team_info())

