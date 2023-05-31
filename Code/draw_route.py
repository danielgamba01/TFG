from pathlib import Path

from rosbags.highlevel import AnyReader

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


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
ax.set_zlim(0,50)
ax.set_xlim(-100,225)
ax.set_ylim(-50,275)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
plt.show()

