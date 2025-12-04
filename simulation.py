from solarsystem import SolarSystem

class Simulation:
    def __init__(self, solarsystem: SolarSystem, width: int, height: int,) -> None:
        self._the_sun: Sun | None = None
        self.planets: list[Planet] = []
        self.gravity: UniversalGravity | None = None

