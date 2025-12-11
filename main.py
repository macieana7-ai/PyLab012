from solarsystem import SolarSystem
from planet import Planet
from simulation import Simulation
from sun import Sun


def main():
    solar_sys = SolarSystem()
    the_sun = Sun(name='MySUN', radius=5, mass=1.989e14, temp=5000))
    solar_sys.add_planet(Planet(name='Earth', radius=22.0, mass=.33, distance=50, x=0, y=50, vel_x=16, vel_y=5, color="blue"))
    solar_sys.add_planet(Planet(name='Mars', radius=22.0, mass=.33, distance=50, x=0, y=50, vel_x=12, vel_y=5, color="red"))
    sim = Simulation(solar_sys, 800, 800, 5000)
    sim.register(the_sun)
    solar_sys.show(sim)
    sim.run()
    solar_sys.show_plaents()


    if __name__ == '__main__':
        main()
