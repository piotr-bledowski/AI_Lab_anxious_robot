import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node
import xacro
import random

def generate_launch_description():
    pkg_robot_description = get_package_share_directory('robot_description')

    xacro_file_name = 'differential_drive_robot.xacro.urdf'

    robot_description_path = os.path.join(pkg_robot_description, 'urdf', xacro_file_name)

    # Where to spawn robot in the Gazebo world
    position = [0.0, 0.0, 0.5]  # [X, Y, Z](
    orientation = [0.0, 0.0, 0.0]  # [R, P, Y]

    base_robot_name = 'diff_drive_robot'
    # Gazebo needs a unique entity name
    entity_name = base_robot_name + '-' + str(random.random())

    # Compile xacro
    robot_description = xacro.process_file(robot_description_path)
    # Stringify the XML file
    xml = robot_description.toxml()

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=[
            '-string', xml,
            '-topic', 'robot_description',
            '-name', entity_name,
            '-x', str(position[0]),
            '-y', str(position[1]),
            '-z', str(position[2]),
            '-R', str(orientation[0]),
            '-P', str(orientation[1]),
            '-Y', str(orientation[2])
        ]
    )

    return LaunchDescription([
        spawn_robot
    ])