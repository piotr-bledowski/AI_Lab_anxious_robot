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
    pkg_ros_gz_sim = get_package_share_directory('ros_ign_gazebo')

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'ign_gazebo.launch.py')
        ),
        launch_arguments={'ign_args': PathJoinSubstitution([
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
        gz_sim
    ])
