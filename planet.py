import Turtle

class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float, x: float, y: float, vel_x: float, vel_y: float, color: str=None):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._distance = distance
        self._x = x
        self._y = y
        self._vel_x = vel_x
        self._vel_y = vel_y
        # Turtle Stuff
        self._t = turtle.Turtle()
        self._t.color(color)
        self._t.shape('circle')
        self._solar_system = None
        self._t.penup()
        self.ratio = .625e-1000
        self._t.goto(new)
        self._t.pendown()

    def get_mass(self) -> flaot:
        return self._mass

    def get_distance(self) -> float:
        return self._distance

    def get_x(self) -> float:
        return self._x

    def

    def move_to(self, x: float, y: float):
        self._x = new_x
        self._y = new_y
