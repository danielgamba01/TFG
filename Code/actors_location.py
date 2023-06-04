# Esto código recorre la lista de actores buscando cuales son vehículos
# o walkers e imprime su ubicacion y orientación. También imprime la
# posición y ubicación del espectador
# Autor: Daniel Steven Gamba Correa

import carla
import time


# Establecer la conexión con el servidor de simulación
client = carla.Client('localhost', 2000)
client.set_timeout(2.0)

# Crear el mundo y esperar a que los actores se carguen
world = client.get_world()
time.sleep(2.0)
#world.unload_map_layer(carla.MapLayer.Buildings)
# Obtener la lista de actores
actor_list = world.get_actors()

# Iterar sobre la lista de actores y obtener la ubicación, orientación y velocidad de los vehículos y peatones
for actor in actor_list:
    if actor.type_id.startswith('spectator'):
        vehicle_location = actor.get_location()
        vehicle_rotation = actor.get_transform().rotation
        print(f"Ubicación del spectator: {vehicle_location}")
        print(f"Orientación del spectator: {vehicle_rotation}\n")
    elif actor.type_id.startswith('walker'):
        pedestrian_location = actor.get_location()
        pedestrian_rotation = actor.get_transform().rotation
        print(f"Ubicación del peatón {actor.id}: {pedestrian_location}")
        print(f"Orientación del peatón {actor.id}: {pedestrian_rotation}\n")
    elif actor.type_id.startswith('vehicle'):
        vehicle_location = actor.get_location()
        vehicle_rotation = actor.get_transform().rotation
        print(f"Ubicación del vehicle {actor.id}: {vehicle_location}")
        print(f"Orientación del vehicle {actor.id}: {vehicle_rotation}\n")

