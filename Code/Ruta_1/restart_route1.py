import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()
bp_lib = world.get_blueprint_library()

# Set up the simulator in synchronous mode
settings = world.get_settings()
settings.synchronous_mode = True # Enables synchronous mode
settings.fixed_delta_seconds = 0.05
world.apply_settings(settings)

# Obtener todos los actores en el mundo
actores = world.get_actors()

# Filtrar los actores que son vehículos
vehiculos=[]
for actor in actores:
        if actor.type_id.startswith('vehicle') or actor.type_id.startswith('walker'):
             vehiculos.append(actor)
# Eliminar los vehículos
for vehiculo in vehiculos:
        vehiculo.destroy()

print("Se eliminaron", len(vehiculos), "actores.")

world.tick()

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


# Spwan Points
spawn_point_1 =  spawn_points[32]
spawn_point_bus =  spawn_points[16]
spawn_point_car_1 =  spawn_points[73]
spawn_point_car_2 =  spawn_points[126]
spawn_point_car_3 =  spawn_points[104]


spawn_point_walker_1=carla.Transform(carla.Location(x=-68.0,y=6.23,z=2.0),carla.Rotation(pitch=0.0, yaw=0.0, roll=0.0))
spawn_point_walker_2= carla.Transform(carla.Location(x=-90.0,y=138.6,z=2.0),carla.Rotation(pitch=0.0, yaw=-130.0, roll=0.0))
spawn_point_walker_3= carla.Transform(carla.Location(x=-90.5,y=138.0,z=2.0),carla.Rotation(pitch=0.0, yaw=-130.0, roll=0.0))
spawn_point_walker_4= carla.Transform(carla.Location(x=-31.4,y=119.5,z=2.0),carla.Rotation(pitch=0.0, yaw=180.0, roll=0.0))
spawn_point_walker_5= carla.Transform(carla.Location(x=-33.0,y=119.5,z=2.0),carla.Rotation(pitch=0.0, yaw=0.0, roll=0.0))

spawn_point_bycicle_1= spawn_points[108]
spawn_point_bycicle_2= carla.Transform(carla.Location(x=4.92,y=127.0,z=1.0),carla.Rotation(pitch=0.0, yaw=0.0, roll=0.0))

print(f'El punto de aparicion del toyota es {spawn_point_1}')
print(f'El punto de aparicion del bus es {spawn_point_bus}')
print(f'El punto de aparicion del car 1 es {spawn_point_car_1}')
print(f'El punto de aparicion del car 2 es {spawn_point_car_2}')
print(f'El punto de aparicion del car 3 es {spawn_point_car_3}')
print(f'El punto de aparicion del walker 1 es {spawn_point_walker_1}')
print(f'El punto de aparicion del walker 2 es {spawn_point_walker_2}')
print(f'El punto de aparicion del walker 3 es {spawn_point_walker_3}')
print(f'El punto de aparicion del walker 4 es {spawn_point_walker_4}')
print(f'El punto de aparicion del walker 5 es {spawn_point_walker_5}')
print(f'El punto de aparicion del bicycle 1 es {spawn_point_bycicle_1}')
print(f'El punto de aparicion del bicycle 2 es {spawn_point_bycicle_2}')

# Spawn the main vehicle
vehicle_bp = bp_lib.find('vehicle.toyota.prius') 
vehicle = world.try_spawn_actor(vehicle_bp, spawn_point_1)

# Spawn others actors
bus_bp=vehicle_bp = bp_lib.find('vehicle.mitsubishi.fusorosa') 
bus= world.try_spawn_actor(bus_bp, spawn_point_bus)

car_1_bp=vehicle_bp = bp_lib.find('vehicle.audi.etron') 
car_1= world.try_spawn_actor(car_1_bp, spawn_point_car_1)

car_2_bp=vehicle_bp = bp_lib.find('vehicle.bmw.grandtourer') 
car_2= world.try_spawn_actor(car_2_bp, spawn_point_car_2)

car_3_bp=vehicle_bp = bp_lib.find('vehicle.audi.a2') 
car_3= world.try_spawn_actor(car_3_bp, spawn_point_car_3)

walker_1_pb=vehicle_bp = bp_lib.find('walker.pedestrian.0003') 
walker_1= world.try_spawn_actor(walker_1_pb, spawn_point_walker_1)
walker_2_pb=vehicle_bp = bp_lib.find('walker.pedestrian.0004') 
walker_2= world.try_spawn_actor(walker_2_pb, spawn_point_walker_2)
walker_3_pb=vehicle_bp = bp_lib.find('walker.pedestrian.0005') 
walker_3= world.try_spawn_actor(walker_3_pb, spawn_point_walker_3)
walker_4_pb=vehicle_bp = bp_lib.find('walker.pedestrian.0001') 
walker_4= world.try_spawn_actor(walker_4_pb, spawn_point_walker_4)
walker_5_pb=vehicle_bp = bp_lib.find('walker.pedestrian.0008') 
walker_5= world.try_spawn_actor(walker_5_pb, spawn_point_walker_5)

bycicle_1_pb=vehicle_bp = bp_lib.find('vehicle.diamondback.century')
bycicle_1= world.try_spawn_actor(bycicle_1_pb, spawn_point_bycicle_1)
bycicle_2_pb=vehicle_bp = bp_lib.find('vehicle.bh.crossbike') 
bycicle_2= world.try_spawn_actor(bycicle_2_pb, spawn_point_bycicle_2)
 
print("Se cargaron los actores.")        
while True:
    world.tick()
    


      
