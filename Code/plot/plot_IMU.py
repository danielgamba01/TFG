# Este código grafica los datos de un sersor IMU que hayan sido guardados en un archivo .bag 
# con anterioridad. Se pueden limitar los datos a un periodo de tiempo si hace falta
# Autor: Daniel Steven Gamba Correa


from pathlib import Path

from rosbags.highlevel import AnyReader

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

import math

PI=math.pi
 
def euler_from_quaternion(x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in degrees (counterclockwise)
        pitch is rotation around y in degrees (counterclockwise)
        yaw is rotation around z in degrees (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)*180/PI
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)*180/PI
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)*180/PI
     
        return roll_x, pitch_y, yaw_z # in degrees
        
        
t=[]
roll_x=[]
pitch_y=[]
yaw_z=[]
t2=[]


x1=[]
y1=[]
z1=[]
# create reader instance and open for reading
with AnyReader([Path('/home/daniel/New_Code/bags/route_21/toyota_other')]) as reader:
    connections = [x for x in reader.connections if x.topic == '/carla/ego_vehicle/Rigth_IMU']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
         msg = reader.deserialize(rawdata, connection.msgtype)
         
         t.append(msg.header.stamp.sec+msg.header.stamp.sec/1000000000)
         alpha,beta,gamma=euler_from_quaternion(msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w)
         roll_x.append(alpha)
         pitch_y.append(beta)
         yaw_z.append(gamma)
         tp=msg.header.stamp.sec+msg.header.stamp.sec/1000000000
         if tp<995.0:
                t2.append(tp)
                x1.append(msg.linear_acceleration.x)
                y1.append(msg.linear_acceleration.y)
                z1.append(msg.linear_acceleration.z)
                #print(f'x= {x},y={y}, z={z}')
         

ax = plt.figure().add_subplot(adjustable='box')
ax.plot(t,roll_x,label="Roll X") 
ax.plot(t,pitch_y,label="Pitch Y")
ax.plot(t,yaw_z,label="Yaw Z")    
#ax.set_xlim(98,130)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Orientation (º)')

ax.legend()

ax1 = plt.figure().add_subplot(adjustable='box')
ax1.plot(t2,x1,label="X") 
ax1.plot(t2,y1,label="Y")
ax1.plot(t2,z1,label="Z")    
#ax1.set_xlim(98,130)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Acceleration (m/s²)')

ax1.legend()

plt.show()

