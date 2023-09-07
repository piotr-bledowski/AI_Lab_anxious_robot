import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import Node

def generate_launch_description():
    # Paths to packages
    robot_description_pkg_path = get_package_share_directory('robot_description')
    launch_config_pkg_path = get_package_share_directory('launch_config')
    simulation_pkg_path = get_package_share_directory('simulation')