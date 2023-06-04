import carla
import time

# Conexión al simulador CARLA
client = carla.Client('localhost', 2000)
world = client.get_world()

# Set up the simulator in synchronous mode
print(client.get_available_maps())
client.load_world('Town03_Opt', reset_settings=True, map_layers=carla.MapLayer.All)

print("Se cambio el mundo.")


