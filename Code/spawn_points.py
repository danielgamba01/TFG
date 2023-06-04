# Este archivo dibuja los puntos de aparición en el mapa
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
"""
print(f'La localizacion del spawn_point 32 es:\n Localizacion: {spawn_points[32].location} \n Rotacion: {spawn_points[32].rotation}')
print(f'La localizacion del spawn_point 16 es:\n Localizacion: {spawn_points[16].location} \n Rotacion: {spawn_points[16].rotation}')
print(f'La localizacion del spawn_point 73 es:\n Localizacion: {spawn_points[73].location} \n Rotacion: {spawn_points[73].rotation}')
print(f'La localizacion del spawn_point 108 es:\n Localizacion: {spawn_points[108].location} \n Rotacion: {spawn_points[108].rotation}')
"""
# Draw the spawn point locations as numbers in the map
for i, spawn_point in enumerate(spawn_points):
    world.debug.draw_string(spawn_point.location, str(i), life_time=600)

