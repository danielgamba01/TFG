
# Este archivo borra todos los actores presentes
# en una simulación de CARLA
# Autor: Daniel Steven Gamba Correa 

import carla

# Conexión al simulador CARLA
client = carla.Client('localhost', 2000)
world = client.get_world()

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

while True:
        world.tick()
