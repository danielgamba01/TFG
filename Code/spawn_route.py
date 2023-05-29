
# Este archivo dibuja los puntos seleccionados sobre el mapa de CARLA
# Sirve para visualizar las rutas predefinidas
# Autor: Daniel Steven Gamba Correa 

import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()

# Set up the simulator in synchronous mode
settings = world.get_settings()
settings.synchronous_mode = True # Enables synchronous mode
settings.fixed_delta_seconds = 0.05
world.apply_settings(settings)

# Set up the TM in synchronous mode
traffic_manager = client.get_trafficmanager()
traffic_manager.set_synchronous_mode(True)

# Set a seed so behaviour can be repeated if necessary
traffic_manager.set_random_device_seed(0)
random.seed(0)

# We will aslo set up the spectator so we can see what we do
spectator = world.get_spectator()
spawn_points = world.get_map().get_spawn_points()


spawn_point =  spawn_points[32]
# Create route from the chosen spawn points
route_indices = [129, 28, 124, 33, 97, 119, 58, 154, 147]
route = []
for ind in route_indices:
    route.append(spawn_points[ind].location)

# Now let's print them in the map so we can see our routes
world.debug.draw_string(spawn_point.location, 'Spawn point', life_time=60, color=carla.Color(255,0,0))

for ind in route_indices:
    spawn_points[ind].location
    world.debug.draw_string(spawn_points[ind].location, str(ind), life_time=60, color=carla.Color(255,0,0))


while True:
    world.tick()

