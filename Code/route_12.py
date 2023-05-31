#!/usr/bin/env python3

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
atributos_weather=carla.WeatherParameters(precipitation=100.0,sun_altitude_angle = 20.0, precipitation_deposits=80.0)
world.set_weather(atributos_weather)
# Set up the TM in synchronous mode
traffic_manager = client.get_trafficmanager()
traffic_manager.set_synchronous_mode(True)

# Set a seed so behaviour can be repeated if necessary
traffic_manager.set_random_device_seed(0)
random.seed(0)

# We will aslo set up the spectator so we can see what we do
spectator = world.get_spectator()
spawn_points = world.get_map().get_spawn_points()
actores = world.get_actors()

#spawn_point_1 =  spawn_points[32]
# Spawn the main vehicle

# Route of ego_vehicle 
# Create route 1 from the chosen spawn points

route_1_indices = [130,137, 90, 75,19,87]
route_1 = []
for ind in route_1_indices:
    route_1.append(spawn_points[ind].location)
 
bus_indices = [87]
bus_route = []
for ind in bus_indices:
    bus_route.append(spawn_points[ind].location)
    
car_1_indices = [78,100,93]
car_1_route = []
for ind in car_1_indices:
    car_1_route.append(spawn_points[ind].location)   
    
car_2_indices = [99,86,120]
car_2_route = []
for ind in car_2_indices:
    car_2_route.append(spawn_points[ind].location)   
    
car_3_indices = [82,142,133]
car_3_route = []
for ind in car_3_indices:
    car_3_route.append(spawn_points[ind].location)   
    
bycicle_1_indices = [24,106,94]
bycicle_1_route = []
for ind in bycicle_1_indices:
    bycicle_1_route.append(spawn_points[ind].location)
    
bycicle_2_route = []
bycicle_2_route.append(spawn_points[124].location)         
    
# Looking for vehicules    

vehicle=[actor for actor in actores if 'vehicle.toyota.prius' in actor.type_id]
toyota=vehicle[0]

vehicle=[actor for actor in actores if 'vehicle.mitsubishi.fusorosa' in actor.type_id]
bus=vehicle[0]
vehicle=[actor for actor in actores if 'vehicle.audi.etron' in actor.type_id]
car_1=vehicle[0]
vehicle=[actor for actor in actores if 'vehicle.bmw.grandtourer' in actor.type_id]
car_2=vehicle[0]
vehicle=[actor for actor in actores if 'vehicle.audi.a2' in actor.type_id]
car_3=vehicle[0]

vehicle=[actor for actor in actores if 'vehicle.diamondback.century' in actor.type_id]
bycicle_1=vehicle[0]
vehicle=[actor for actor in actores if 'vehicle.bh.crossbike' in actor.type_id]
bycicle_2=vehicle[0]

walker=[actor for actor in actores if 'walker.pedestrian.0003' in actor.type_id]
walker_1=walker[0]
walker=[actor for actor in actores if 'walker.pedestrian.0004' in actor.type_id]
walker_2=walker[0]
walker=[actor for actor in actores if 'walker.pedestrian.0005' in actor.type_id]
walker_3=walker[0]

walker_controller_bp = world.get_blueprint_library().find('controller.ai.walker')
walker_1_control=world.try_spawn_actor(walker_controller_bp, carla.Transform(), walker_1)
walker_2_control=world.try_spawn_actor(walker_controller_bp, carla.Transform(), walker_2)
walker_3_control=world.try_spawn_actor(walker_controller_bp, carla.Transform(), walker_3)

# Route pederestian crossing road (walker_1)
pointw1_1=carla.Location(x=-93.0,y=3.9,z=1.0)
pointw1_2=carla.Location(x=-93.0,y=34.4,z=1.0)
walker_1_control.start()
#walker_1_control.set_max_speed(0.5)
target_pos_w1=pointw1_1
walker_1_control.go_to_location(target_pos_w1)
alt_w1=1

# Route pederestian crossing road (walker_1)
pointw2_1=carla.Location(x=-107.0,y=119.0,z=1.0)
pointw2_2=carla.Location(x=--15.0,y=146.5,z=1.0)
walker_2_control.start()
#walker_1_control.set_max_speed(0.5)
target_pos_w2=pointw2_1
target_pos_w3=pointw2_1
walker_2_control.go_to_location(target_pos_w2)
walker_3_control.start()
walker_3_control.go_to_location(target_pos_w3)




# Set delay to create gap between spawn times
question_delay = 100
counter = question_delay
speed_prct=60
margen=2.0
"""
pose_spect=toyota.get_transform();
pose_spect.location.z+=2.0;
spectator.set_transform(pose_spect)
"""
while True:
    world.tick()

    if toyota.is_alive:
        toyota.set_autopilot(True) # Give TM control over vehicle
        traffic_manager.update_vehicle_lights(toyota, True)
        traffic_manager.random_right_lanechange_percentage(toyota,0.0)
        traffic_manager.random_left_lanechange_percentage(toyota,0.0)  
        traffic_manager.auto_lane_change(toyota, False)   
        #traffic_manager.set_desired_speed(toyota, 10.0)
        
        # Do the route
        traffic_manager.set_path(toyota, route_1)
        
        actual_pos=toyota.get_location()
        final_pos=route_1[-1]
        dist=math.pow(actual_pos.x-final_pos.x,2)+math.pow(actual_pos.y-final_pos.y,2)+math.pow(actual_pos.z-final_pos.z,2)
        if dist < margen:
                toyota.destroy()


    if bus.is_alive:
        bus.set_autopilot(True) # Give TM control over vehicle        
        # Set parameters of TM vehicle control, we don't want lane changes
        traffic_manager.random_right_lanechange_percentage(bus,0.0)
        traffic_manager.random_left_lanechange_percentage(bus,0.0)  
        traffic_manager.auto_lane_change(bus, False) 
        # Do the route
        traffic_manager.set_path(bus, bus_route)
        actual_pos=bus.get_location()
        final_pos=bus_route[-1]
        dist=math.pow(actual_pos.x-final_pos.x,2)+math.pow(actual_pos.y-final_pos.y,2)+math.pow(actual_pos.z-final_pos.z,2)
        if dist < margen:
                bus.destroy()
        
    if car_1.is_alive:
        car_1.set_autopilot(True) # Give TM control over vehicle        
        # Set parameters of TM vehicle control, we don't want lane changes
        traffic_manager.random_right_lanechange_percentage(car_1,0.0)
        traffic_manager.random_left_lanechange_percentage(car_1,0.0)  
        traffic_manager.auto_lane_change(car_1, False) 
        # Do the route
        traffic_manager.set_path(car_1, car_1_route)
        actual_pos=car_1.get_location()
        final_pos=car_1_route[-1]
        dist=math.pow(actual_pos.x-final_pos.x,2)+math.pow(actual_pos.y-final_pos.y,2)+math.pow(actual_pos.z-final_pos.z,2)
        if dist < margen:
                car_1.destroy()
        
    if car_2.is_alive:
        car_2.set_autopilot(True) # Give TM control over vehicle        
        # Set parameters of TM vehicle control, we don't want lane changes
        traffic_manager.random_right_lanechange_percentage(car_2,0.0)
        traffic_manager.random_left_lanechange_percentage(car_2,0.0)  
        traffic_manager.auto_lane_change(car_2, False) 
        # Do the route
        traffic_manager.set_path(car_2, car_2_route)
        
        actual_pos=car_2.get_location()
        final_pos=car_2_route[-1]
        dist=math.pow(actual_pos.x-final_pos.x,2)+math.pow(actual_pos.y-final_pos.y,2)+math.pow(actual_pos.z-final_pos.z,2)
        if dist < margen:
                car_2.destroy()
        
    if car_3.is_alive:
        car_3.set_autopilot(True) # Give TM control over vehicle        
        # Set parameters of TM vehicle control, we don't want lane changes
        traffic_manager.random_right_lanechange_percentage(car_3,0.0)
        traffic_manager.random_left_lanechange_percentage(car_3,0.0)  
        traffic_manager.auto_lane_change(car_3, False) 
        # Do the route
        traffic_manager.set_path(car_3, car_3_route)
        
        actual_pos=car_3.get_location()
        final_pos=car_3_route[-1]
        dist=math.pow(actual_pos.x-final_pos.x,2)+math.pow(actual_pos.y-final_pos.y,2)+math.pow(actual_pos.z-final_pos.z,2)
        if dist < margen:
                car_3.destroy()
           
    if bycicle_1.is_alive:
        bycicle_1.set_autopilot(True) # Give TM control over vehicle        
        # Set parameters of TM vehicle control, we don't want lane changes
        traffic_manager.random_right_lanechange_percentage(bycicle_1,0.0)
        traffic_manager.random_left_lanechange_percentage(bycicle_1,0.0)  
        traffic_manager.auto_lane_change(bycicle_1, False) 
        # Do the route
        traffic_manager.set_path(bycicle_1, bycicle_1_route)
        
        actual_pos=bycicle_1.get_location()
        final_pos=bycicle_1_route[-1]
        dist=math.pow(actual_pos.x-final_pos.x,2)+math.pow(actual_pos.y-final_pos.y,2)+math.pow(actual_pos.z-final_pos.z,2)
        if dist < margen:
                bycicle_1.destroy()
        
    if bycicle_2.is_alive:
        bycicle_2.set_autopilot(True) # Give TM control over vehicle        
        # Set parameters of TM vehicle control, we don't want lane changes
        traffic_manager.random_right_lanechange_percentage(bycicle_2,0.0)
        traffic_manager.random_left_lanechange_percentage(bycicle_2,0.0)  
        traffic_manager.auto_lane_change(bycicle_2, False) 
        # Do the route
        traffic_manager.set_path(bycicle_2, bycicle_2_route)
        
        actual_pos=bycicle_2.get_location()
        final_pos=bycicle_2_route[-1]
        dist=math.pow(actual_pos.x-final_pos.x,2)+math.pow(actual_pos.y-final_pos.y,2)+math.pow(actual_pos.z-final_pos.z,2)
        if dist < margen:
                bycicle_2.destroy()
        
    if walker_1.is_alive:
        actual_pos=walker_1.get_location()
        dist=math.pow(actual_pos.x-target_pos_w1.x,2)+math.pow(actual_pos.y-target_pos_w1.y,2)+math.pow(actual_pos.z-target_pos_w1.z,2)
        if dist < margen:
                if alt_w1:
                        target_pos_w1=pointw1_2
                        alt_w1=0
                else:
                        target_pos_w1=pointw1_1
                        alt_w1=1

                walker_1_control.go_to_location(target_pos_w1)
    
    if walker_2.is_alive:
        actual_pos=walker_2.get_location()
        dist=math.pow(actual_pos.x-target_pos_w2.x,2)+math.pow(actual_pos.y-target_pos_w2.y,2)+math.pow(actual_pos.z-target_pos_w2.z,2)
        if dist < margen:
                #walker_2.destroy()
                target_pos_w2=pointw2_2
                walker_2_control.go_to_location(target_pos_w2)
    if walker_3.is_alive:
        actual_pos=walker_3.get_location()
        dist=math.pow(actual_pos.x-target_pos_w3.x,2)+math.pow(actual_pos.y-target_pos_w3.y,2)+math.pow(actual_pos.z-target_pos_w3.z,2)
        if dist < margen:
                target_pos_w3=pointw2_2
                walker_3_control.go_to_location(target_pos_w3)
       
      
