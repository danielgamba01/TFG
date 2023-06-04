# Este código grafica los datos de un sersor GNSS que hayan sido guardados en un archivo .bag 
# con anterioridad. Se pueden limitar los datos a un periodo de tiempo si hace falta
# Autor: Daniel Steven Gamba Correa

from pathlib import Path

from rosbags.highlevel import AnyReader

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

t=[]
x=[]
y=[]
z=[]

# create reader instance and open for reading
with AnyReader([Path('/home/daniel/New_Code/bags/route_11/actors_all2')]) as reader:
    connections = [x for x in reader.connections if x.topic == '/carla/ego_vehicle/Left_GNSS']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
         msg = reader.deserialize(rawdata, connection.msgtype)
         tp=msg.header.stamp.sec+msg.header.stamp.sec/1000000000
         if tp<250.0:
                t.append(tp)
                x.append(msg.latitude)
                y.append(msg.longitude)
                z.append(msg.altitude)
         
         #print(f'x= {x},y={y}, z={z}')
         

ax = plt.figure().add_subplot(adjustable='box')
ax.plot(y,x) 
ax.set_xlabel('Longitud (º)')
ax.set_ylabel('Latitude (º)')

ax1 = plt.figure().add_subplot(adjustable='box')
ax1.plot(t,z) 
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Altitude (m)')
ax1.set_ylim(0,5)

plt.show()

