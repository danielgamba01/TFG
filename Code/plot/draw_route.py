# Este código dibuja la ruta que haya sido guardada en un archivo .bag 
# con anterioridad. Este código define los ejes de tal manera que se respeten
# las proporciones del recorrido en el eje X e Y. Mientras que en el eje Z se 
# utiliza una mayor escala.
# Autor: Daniel Steven Gamba Correa


from pathlib import Path

from rosbags.highlevel import AnyReader

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

x=[]
y=[]
z=[]
# create reader instance and open for reading
with AnyReader([Path('/home/daniel/New_Code/bags/position2_bag')]) as reader:
    connections = [x for x in reader.connections if x.topic == '/carla/actor/position']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
         msg = reader.deserialize(rawdata, connection.msgtype)
         if msg.x!=0.0 and msg.y!=0.0 and msg.z!=0.0:
                x.append(msg.x)
                y.append(msg.y)
                z.append(msg.z)
         #print(f'x= {x},y={y}, z={z}')
         

ax = plt.figure().add_subplot(projection='3d',adjustable='box')
ax.plot(x, y, z)  # Plot contour curves

x_max=np.amax(x)
y_max=np.amax(y)
z_max=np.amax(z)

x_min=np.amin(x)
y_min=np.amin(y)
z_min=np.amin(z)
if x_max > y_max:
        maximo=x_max+50
else:
        maximo=y_max+50
        
if x_min < y_min:
        minimo=x_min-50
else:
        minimo=y_min-50
print (f'Maximo: {maximo} y minimo: {minimo}')

ax.set_zlim(z_min-5,z_max+30)
ax.set_xlim(minimo,maximo)
ax.set_ylim(minimo,maximo)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
plt.show()

