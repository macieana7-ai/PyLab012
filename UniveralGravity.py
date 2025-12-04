classDiagram

class UniversalGravity:{ +float G}:

class Sun {
-string name
-float radius
-float mass
-float temp
-float x
-float y
+get_mass() float
+get_x_pos() float
+get_y_pos() float
+__str__() string
}


class Planet {
-string name
-float radius
-float mass
-float distance
-float x
-float y
-float vel_x
-float vel_y
+get_mass() float
+get_distance() float
+get_x_pos() float
+get_x_vel() float
+get_y_pos() float
+get_y_vel() float
+set_x_vel(new_x_vel: float

)
+set_y_vel(new_y_vel: float)
+move_to(new_x: float, new_y: float)
+__str__()
string
}

class SolarSystem {
-Sun the_sun
-list~Planet~ planets
+add_planet(new_planet: Planet

)
+add_sun(the_sun: Sun)
+show_planets()
+ move_planets()
}

class Simulation {
-SolarSystem solar_system
-int width
-int height
-int num_periods
+run()
}


UniversalGravity < -- SolarSystem: uses
Sun - - * SolarSystem: manages
Planet - - * SolarSystem: manages
SolarSystem < -- * Simulation: run
