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
    pkg_robot_description = get_package_share_directory('robot_description')
    pkg_launch_config = get_package_share_directory('launch_config')
    pkg_simulation = get_package_share_directory('simulation')

    start_rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_launch_config, 'launch', 'rviz.launch.py'),
        )
    )

    start_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_launch_config, 'launch', 'gazebo_world.launch.py'),
        )
    )

    spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_launch_config, 'launch', 'spawn_robot.launch.py'),
        )
    )

    ros_gz_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': os.path.join(pkg_launch_config, 'config', 'ros_gz_bridge_config.yaml')
        }],
        output='screen'
    )

    return LaunchDescription([
        start_rviz,
        start_gazebo,
        spawn_robot,
        ros_gz_bridge
    ])
