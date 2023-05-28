from pathlib import Path

from rosbags.highlevel import AnyReader

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


x=[]
y=[]
z=[]
# create reader instance and open for reading
with AnyReader([Path('/home/daniel/New_Code/bags/position_bag')]) as reader:
    connections = [x for x in reader.connections if x.topic == '/carla/actor/position']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
         msg = reader.deserialize(rawdata, connection.msgtype)
         x.append(msg.x)
         y.append(msg.y)
         z.append(msg.z)
         #print(f'x= {x},y={y}, z={z}')
         

ax = plt.figure().add_subplot(projection='3d')
ax.plot(x, y, z)  # Plot contour curves
ax.set_zlim(0,2)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
plt.show()

