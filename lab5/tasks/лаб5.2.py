class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
         self.radius = new_radius

c = Circle(13)
c.set_radius(20)
print(c.get_radius())
