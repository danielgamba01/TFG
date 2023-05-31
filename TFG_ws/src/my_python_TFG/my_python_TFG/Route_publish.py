#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

import carla
import numpy


class RoutePublish(Node):
                
        def __init__(self):
                super().__init__('publish_route')
                pub_topic = f'/carla/actor/position'
                self.publisher = self.create_publisher(msg_type=Point, topic=pub_topic, qos_profile=10)
                time_period=0.5
                
                # Conectarse al servidor de Carla
                client = carla.Client('localhost', 2000)
                client.set_timeout(10.0)

                # Obtener el mundo de Carla
                self.world = client.get_world()

                # Set up the simulator in synchronous mode
                """
                settings = self.world.get_settings()
                settings.synchronous_mode = True # Enables synchronous mode
                settings.fixed_delta_seconds = 0.05
                self.world.apply_settings(settings)
                """   
                actor_list = self.world.get_actors()

                vehicle=[actor for actor in actor_list if 'vehicle.toyota.prius' in actor.type_id]
                self.vehicle=vehicle[0]
                
                timer_period = 0.5  # seconds
                self.timer = self.create_timer(timer_period, self.publish_method)
          

        def publish_method(self):                
                
                position=Point()
                self.pose_vehicle=self.vehicle.get_location()
                position.x=self.pose_vehicle.x
                position.y=-self.pose_vehicle.y
                position.z=self.pose_vehicle.z

                # we take the opposite of y axis
                # (as lidar point are express in left handed coordinate system, and ros need right handed)
                self.publisher.publish(position)
                print(f'La poscion del vehiculo es x={self.pose_vehicle.x}, y={self.pose_vehicle.y}, z={self.pose_vehicle.z}')
                      
    


def main(args=None):
    rclpy.init(args=args)

    node = RoutePublish()
    
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
