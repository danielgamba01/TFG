# Este codigo realiza una ruta para un peaton. La ruta consiste en dar indefinidamente
# vueltas a una manzana. Para ello se han definido 3 puntos y se va alternando el objetivo
# del peaton entre estos 3 dependiendo de donde se encuentre.
# Autor: Daniel Steven Gamba Correa

import carla
import random
import math

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()
bp_lib = world.get_blueprint_library()

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

# Set the spawn point of walker
spawn_point_walker_1=carla.Transform(carla.Location(x=-63.0,y=6.23,z=2.0),carla.Rotation(pitch=0.0, yaw=0.0, roll=0.0))

# Spawn walker
walker_1_pb= bp_lib.find('walker.pedestrian.0003') 
walker_1= world.try_spawn_actor(walker_1_pb, spawn_point_walker_1)
world.tick()
# Set the walker's control
walker_controller_bp = bp_lib.find('controller.ai.walker')
walker_1_control=world.try_spawn_actor(walker_controller_bp, carla.Transform(), walker_1)
world.tick()

point1=carla.Location(x=-86.9,y=6,z=2.0)
point2=carla.Location(x=-81.6,y=-46.3,z=2.0)
point3=carla.Location(x=-59.0,y=-1.5,z=2.0)

target_pos=point1
walker_1_control.start()
walker_1_control.go_to_location(target_pos)
world.tick()
alt=1
margen=2.0
while True:
    world.tick()
    if walker_1.is_alive:
        actual_pos=walker_1.get_location()
        dist=math.pow(actual_pos.x-target_pos.x,2)+math.pow(actual_pos.y-target_pos.y,2)+math.pow(actual_pos.z-target_pos.z,2)
        if dist < margen:
                if alt==1:
                        target_pos=point2
                        alt=2
                elif alt==2:
                        target_pos=point3
                        alt=3
                else:
                        target_pos=point1
                        alt=1
                walker_1_control.go_to_location(target_pos)
        


