from Sun import Sun
from planet import Planet
from UniveralGravity import UniveralGravity
from typing import List
from math import sqrt

class SolarSystem:
    def __init__(self):


   def add_sun(self, the_sun: Sun):
       self._the_sun = the_sun

   def show_planet(self):
       for p in self._planets:
           print(p)

   def move_planets(self):
       dt = .1  # Constant time interval for each solar system iteration.
       ug = UniveralGravity(6.67430e-11)

       for planet in self._planets:
           # Move the distance covered in the interval dt
           planet.move_to(
               planet.get_x_pos() + dt * planet.get_x_vel(),
               planet.get_y_pos() + dt * planet.get_y_vel())

           # After move we need to calculate the new distance from the sun using the distance formula.
           dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
           dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
           new_distance = math.sqrt(dist_x ** 2 + dist_y ** 2)

           # Let's calculate our new acceleration so we can set our new velocity
           acc_x = ug.G * self.the_sun.get_mass() * dist_x / new_distance ** 3
           acc_y = ug.G * self.the_sun.get_mass() * dist_y / new_distance ** 3

           # Now let's calculate the new x and y velocities and update them for the planet
           planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
           planet.set_y_vel(planet.get_y_vel() + dt * acc_y)