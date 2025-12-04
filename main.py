from solarsystem import SolarSystem
from planet import Planet
from simulation import Simulation
from sun import Sun


def main():
    solar_sys = SolarSystem()
    solar_sys.add_sun(Sun(name='MySUN', radius=100, mass=100, temp=100))
    solar_sys.add_planet(Planet(name='OhNo', radius=22.0, mass=.33, temp=100, pressure=100, distance=100, x=10, y=0, vel_x=100, vel_y=100))
    sim = Simulation(solar_sys,500, 500, 100)
    solar_sys.show(sim)
    sim.run()
    solar_sys.show_plaents()


    if __name__ == '__main__':
       main()
