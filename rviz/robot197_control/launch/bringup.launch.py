from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
import os


def generate_launch_description():

    robot_description_package = 'my_robot_description'
    xacro_file = 'robot197.xacro'

    xacro_path = os.path.join(
        get_package_share_directory(robot_description_package),
        'urdf',
        xacro_file
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': ParameterValue(
                Command(['xacro ', xacro_path]),
                value_type=str
            )
        }]
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen'
    )

    controller = Node(
        package='robot197_control',
        executable='simple_controller',
        name='simple_joint_controller',
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher,
        rviz,
        controller
    ])
