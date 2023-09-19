import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution

from launch_ros.actions import Node

def generate_launch_description():
    # Paths to packages
    pkg_simulation = get_package_share_directory('simulation')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    gazebo_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world_name': PathJoinSubstitution([
            pkg_simulation,
            'worlds',
            'empty.sdf'
        ])}.items(),
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=[os.path.join(pkg_simulation, 'worlds', 'empty.sdf'), ''],
            description='SDF world file'
        ),
        gazebo_sim
    ])
