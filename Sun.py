class Sun:

    def __init__(self, name:str, radius:float, mass:float, temp:float, x:int, y:int):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = x
        self.y = y

    def get_mass(self): -> float:
        return self_mass

    def get_x_pos(self) -> int:
        return self.x

    def get_y_pos(self) -> int:
        return self.y

    def __str__(self):
        return f'''Sun(
{self.name}, 
{self.x}, 
{self.y})'''

