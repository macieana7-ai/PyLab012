import turtle

class Sun:
    def __init__(self, name:str, radius:float, mass:float, temp:float, x:int, y:int, icon:srt):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = x
        self.y = y
        # Turtle Stuff
        self._t =turtle.Turtle()
        self._t.color('yellow')
        self._t.shape('circle')
        self._t.goto(self.x, self.y)
        self.icon()

    def get_mass(self) -> float:
        return self_mass

    def get_x_pos(self) -> int:
        return self._x

    def get_y_pos(self) -> int:
        return self._y

   def updater(self, obj, event:str):
       obj.get_screen().addShape(self.icon)
       self._t.shape('sun.gif')

    def __str__(self):
        return f'''Sun(name={self.name}, radius={self.radius}, mass={self.mass}, temp={self.temp})f'temp={self.temp},x={self.x},y={self.y})'''

