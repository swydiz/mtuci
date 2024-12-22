class Vehicle:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
    def get_info(self):
        return self.mark, self.model

class Car(Vehicle):
    def __init__(self, mark, model, fuel):
        self.fuel = fuel
        super().__init__(mark, model)
    def fuel_type(self):
        return super().get_info(), self.fuel

b = Vehicle('aaa', 'fff')
c = Car('aa', 'ff', 'ddd')
print(b.get_info(), c.fuel_type())
