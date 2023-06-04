#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
from carla_ros_bridge.sensor import create_cloud 
import std_msgs.msg
from rosgraph_msgs.msg import Clock

import carla
import numpy
import time


class LidarFusion(Node):
    
        def process_lidar_data_0(self,data):
                # Convertir los datos de sensor de formato carla.LidarMeasurement a una matriz numpy
                lidar_data = numpy.frombuffer(
                        bytes(data.raw_data), dtype=numpy.float32)
                lidar_data = numpy.reshape(lidar_data, (int(lidar_data.shape[0] / 4), 4))
                lidar_data = numpy.copy(lidar_data)
                lidar_data[:, 1] *= -1
                self.lidar_data_0 = lidar_data
                
        def process_lidar_data_1(self,data):
                # Convertir los datos de sensor de formato carla.LidarMeasurement a una matriz numpy
                lidar_data = numpy.frombuffer(
                        bytes(data.raw_data), dtype=numpy.float32)
                lidar_data = numpy.reshape(lidar_data, (int(lidar_data.shape[0] / 4), 4))
                lidar_data = numpy.copy(lidar_data)
                lidar_data[:, 1] *= -1
                self.lidar_data_1 = lidar_data

        def process_lidar_data_2(self,data):
                # Convertir los datos de sensor de formato carla.LidarMeasurement a una matriz numpy
                lidar_data = numpy.frombuffer(
                        bytes(data.raw_data), dtype=numpy.float32)
                lidar_data = numpy.reshape(lidar_data, (int(lidar_data.shape[0] / 4), 4))
                lidar_data = numpy.copy(lidar_data)
                lidar_data[:, 1] *= -1
                self.lidar_data_2 = lidar_data
                
        def process_lidar_data_3(self,data):
                # Convertir los datos de sensor de formato carla.LidarMeasurement a una matriz numpy
                lidar_data = numpy.frombuffer(
                        bytes(data.raw_data), dtype=numpy.float32)
                lidar_data = numpy.reshape(lidar_data, (int(lidar_data.shape[0] / 4), 4))
                lidar_data = numpy.copy(lidar_data)
                lidar_data[:, 1] *= -1
                self.lidar_data_3 = lidar_data
                        
        def process_lidar_data_4(self,data):
                # Convertir los datos de sensor de formato carla.LidarMeasurement a una matriz numpy
                lidar_data = numpy.frombuffer(
                        bytes(data.raw_data), dtype=numpy.float32)
                lidar_data = numpy.reshape(lidar_data, (int(lidar_data.shape[0] / 4), 4))
                lidar_data = numpy.copy(lidar_data)
                lidar_data[:, 1] *= -1
                self.lidar_data_4 = lidar_data
                
                
        def process_lidar_data_5(self,data):
                # Convertir los datos de sensor de formato carla.LidarMeasurement a una matriz numpy
                lidar_data = numpy.frombuffer(
                        bytes(data.raw_data), dtype=numpy.float32)
                lidar_data = numpy.reshape(lidar_data, (int(lidar_data.shape[0] / 4), 4))
                lidar_data = numpy.copy(lidar_data)
                lidar_data[:, 1] *= -1
                self.lidar_data_5 = lidar_data
                
        def process_lidar_data_6(self,data):
                # Convertir los datos de sensor de formato carla.LidarMeasurement a una matriz numpy
                lidar_data = numpy.frombuffer(
                        bytes(data.raw_data), dtype=numpy.float32)
                lidar_data = numpy.reshape(lidar_data, (int(lidar_data.shape[0] / 4), 4))
                lidar_data = numpy.copy(lidar_data)
                lidar_data[:, 1] *= -1
                self.lidar_data_6 = lidar_data
                
        def process_lidar_data_7(self,data):
                # Convertir los datos de sensor de formato carla.LidarMeasurement a una matriz numpy
                lidar_data = numpy.frombuffer(
                        bytes(data.raw_data), dtype=numpy.float32)
                lidar_data = numpy.reshape(lidar_data, (int(lidar_data.shape[0] / 4), 4))
                lidar_data = numpy.copy(lidar_data)
                lidar_data[:, 1] *= -1
                self.lidar_data_7 = lidar_data
                
        def __init__(self):
                super().__init__('lidar_fusion')
                # Inicializar variables
                self.lidar_data_0 = None
                self.lidar_data_1 = None
                self.lidar_data_2 = None
                self.lidar_data_3 = None
                self.lidar_data_4 = None
                self.lidar_data_5 = None
                self.lidar_data_6 = None
                self.lidar_data_7 = None
                all_lidar_data=[] 
                self.id_array=[0,0,0,0,0,0,0,0]
                
                #Crear al publisher
                pub_topic = f'/carla/ego_vehicle/LIDAR'
                self.publisher = self.create_publisher(msg_type=PointCloud2, topic=pub_topic, qos_profile=10)
                
                #Crea un subscriptor para sincronizarse
                self.subscription = self.create_subscription(Clock, 'clock',self.publish_method, 10)

                # Conectarse al servidor de Carla
                client = carla.Client('localhost', 2000)
                client.set_timeout(10.0)

                # Obtener el mundo de Carla
                self.world = client.get_world()

                # Activar el modo síncrono
                settings = self.world.get_settings()
                settings.synchronous_mode = True # Enables synchronous mode
                settings.fixed_delta_seconds = 0.05
                self.world.apply_settings(settings)
                   
                actor_list = self.world.get_actors()

                for actor in actor_list:
                    # Guarda los id de cada uno de los sensores Lidar
                    if actor.type_id.startswith('sensor'):
                        sensor_name = actor.attributes.get('role_name')
                        #print(f'El nombre del sensor es {sensor_name}')
                        if sensor_name== "LIDAR_0":
                                print(f"El Front tiene un ID= {actor.id}")
                                self.id_array[0]=actor.id
                        if sensor_name== "LIDAR_1":
                                print(f"El LIDAR 1 tiene un ID= {actor.id}")
                                self.id_array[1]=actor.id
                        if sensor_name== "LIDAR_2":
                                print(f"El LIDAR 2 tiene un ID= {actor.id}")
                                self.id_array[2]=actor.id
                        if sensor_name== "LIDAR_3":
                                print(f"El LIDAR 3 tiene un ID= {actor.id}")
                                self.id_array[3]=actor.id
                        if sensor_name== "LIDAR_4":
                                print(f"El LIDAR 4 tiene un ID= {actor.id}")
                                self.id_array[4]=actor.id
                        if sensor_name== "LIDAR_5":
                                print(f"El LIDAR 5 tiene un ID= {actor.id}")
                                self.id_array[5]=actor.id
                        if sensor_name== "LIDAR_6":
                                print(f"El LIDAR 6 tiene un ID= {actor.id}")
                                self.id_array[6]=actor.id
                        if sensor_name== "LIDAR_7":
                                print(f"El LIDAR 7 tiene un ID= {actor.id}")
                                self.id_array[7]=actor.id
                                
                # Llama a las funciones de cada uno de los lidar
                lidar_actor_0=self.world.get_actor(self.id_array[0])
                lidar_actor_0.listen(self.process_lidar_data_0)
                
                lidar_actor_1=self.world.get_actor(self.id_array[1])
                lidar_actor_1.listen(self.process_lidar_data_1)

                lidar_actor_2=self.world.get_actor(self.id_array[2])
                lidar_actor_2.listen(self.process_lidar_data_2)
                
                lidar_actor_3=self.world.get_actor(self.id_array[3])
                lidar_actor_3.listen(self.process_lidar_data_3)

                lidar_actor_4=self.world.get_actor(self.id_array[4])
                lidar_actor_4.listen(self.process_lidar_data_4)

                lidar_actor_5=self.world.get_actor(self.id_array[5])
                lidar_actor_5.listen(self.process_lidar_data_5)

                lidar_actor_6=self.world.get_actor(self.id_array[6])
                lidar_actor_6.listen(self.process_lidar_data_6)

                lidar_actor_7=self.world.get_actor(self.id_array[7])
                lidar_actor_7.listen(self.process_lidar_data_7)
                
                time.sleep(2.0)

        def publish_method(self,msg):

                # Une la información de todos los Lidar's
                all_lidar_data=numpy.concatenate((self.lidar_data_0,self.lidar_data_1),axis=0)
                all_lidar_data=numpy.concatenate((all_lidar_data,self.lidar_data_2),axis=0)
                all_lidar_data=numpy.concatenate((all_lidar_data,self.lidar_data_3),axis=0)
                all_lidar_data=numpy.concatenate((all_lidar_data,self.lidar_data_4),axis=0)
                all_lidar_data=numpy.concatenate((all_lidar_data,self.lidar_data_5),axis=0)
                all_lidar_data=numpy.concatenate((all_lidar_data,self.lidar_data_6),axis=0)
                all_lidar_data=numpy.concatenate((all_lidar_data,self.lidar_data_7),axis=0)
                        
                #print(f'Datos del LIDAR_0: {self.lidar_data_0}')

                # Cada 20 instantes de la simulacion genera el mensaje y lo publica en ROS
                lidar_msg=PointCloud2() 
                lidar_msg.header.stamp.sec = msg.clock.sec
                lidar_msg.header.stamp.nanosec = msg.clock.nanosec
                lidar_msg.header.frame_id='ego_vehicle/LIDAR'
                fields = [
                    PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
                    PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
                    PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
                    PointField(name='intensity', offset=12, datatype=PointField.FLOAT32, count=1)
                ]

                # we take the opposite of y axis
                # (as lidar point are express in left handed coordinate system, and ros need right handed)
                point_cloud_msg = create_cloud(lidar_msg.header, fields, all_lidar_data)
                self.publisher.publish(point_cloud_msg)
                print('Ha publicado')

    


def main(args=None):
    rclpy.init(args=args)

    lidar_fusion = LidarFusion()
    
    rclpy.spin(lidar_fusion)

    LidarFusion.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

