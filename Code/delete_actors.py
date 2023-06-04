# Este archivo borra todos los actores de la simulación
#Autor: Daniel Steven Gamba Correa

import carla

# Conexión al simulador CARLA
client = carla.Client('localhost', 2000)
world = client.get_world()


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


