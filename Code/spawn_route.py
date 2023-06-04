# Este archivo dibuja los puntos de las rutas que se le especifique
# Autor: CARLA Simulator

import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()


# Set up the TM in synchronous mode
traffic_manager = client.get_trafficmanager()
traffic_manager.set_synchronous_mode(True)

# Set a seed so behaviour can be repeated if necessary
traffic_manager.set_random_device_seed(0)
random.seed(0)

# We will aslo set up the spectator so we can see what we do
spectator = world.get_spectator()
spawn_points = world.get_map().get_spawn_points()


spawn_point_1 =  spawn_points[88]
spawn_point_bus =  spawn_points[133]
spawn_point_car_1 =  spawn_points[241]
spawn_point_car_2 =  spawn_points[130]
spawn_point_car_3 =  spawn_points[60]
spawn_point_bycicle_1= spawn_points[177]
spawn_point_bycicle_2= spawn_points[2]

# Create route from the chosen spawn points
bus_indices = [234,204]
car_1_indices = [225,241,225,241,225]
car_2_indices = [71,195]
car_3_indices = [3,172]
bycicle_1_indices = [243]
bycicle_2_indices = [4,236,2]

tiempo=300

# Now let's print them in the map so we can see our routes
world.debug.draw_string(spawn_point_bus.location, 'Spawn point', life_time=tiempo, color=carla.Color(255,0,0))
world.debug.draw_string(spawn_point_car_1.location, 'Spawn point', life_time=tiempo, color=carla.Color(0,255,0))
world.debug.draw_string(spawn_point_car_2.location, 'Spawn point', life_time=tiempo, color=carla.Color(0,0,255))
world.debug.draw_string(spawn_point_car_3.location, 'Spawn point', life_time=tiempo, color=carla.Color(255,255,0))
world.debug.draw_string(spawn_point_bycicle_1.location, 'Spawn point', life_time=tiempo, color=carla.Color(255,0,255))
world.debug.draw_string(spawn_point_bycicle_2.location, 'Spawn point', life_time=tiempo, color=carla.Color(0,255,255))


for ind in bus_indices:
    spawn_points[ind].location
    world.debug.draw_string(spawn_points[ind].location, str(ind), life_time=tiempo, color=carla.Color(255,0,0))
for ind in car_1_indices:
    spawn_points[ind].location
    world.debug.draw_string(spawn_points[ind].location, str(ind), life_time=tiempo, color=carla.Color(0,255,0))
for ind in car_2_indices:
    spawn_points[ind].location
    world.debug.draw_string(spawn_points[ind].location, str(ind), life_time=tiempo, color=carla.Color(0,0,255))
for ind in car_3_indices:
    spawn_points[ind].location
    world.debug.draw_string(spawn_points[ind].location, str(ind), life_time=tiempo, color=carla.Color(255,255,0))
for ind in bycicle_1_indices:
    spawn_points[ind].location
    world.debug.draw_string(spawn_points[ind].location, str(ind), life_time=tiempo, color=carla.Color(255,0,255))
for ind in bycicle_2_indices:
    spawn_points[ind].location
    world.debug.draw_string(spawn_points[ind].location, str(ind), life_time=tiempo, color=carla.Color(0,255,255))
    


