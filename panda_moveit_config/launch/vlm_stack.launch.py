from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_desc = get_package_share_directory('panda_description')
    world = os.path.join(pkg_desc,'worlds','panda_workspace.sdf')
    model = os.path.join(pkg_desc,'panda','model.sdf')

    base = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('panda_moveit_config'),'launch','ex_ign_control.launch.py'])
        ),
        launch_arguments={'world':world,'model':model,'ign_verbosity':'3','use_sim_time':'true'}.items()
    )

    cam_bridge = Node(
        package='ros_ign_bridge', executable='parameter_bridge', output='screen',
        arguments=[
            'WristCamera/image@sensor_msgs/msg/Image@ignition.msgs.Image',
            'WristCamera/camera_info@sensor_msgs/msg/CameraInfo@ignition.msgs.CameraInfo'
        ],
        parameters=[{'use_sim_time': True}],
    )

    perception = Node(package='panda_vlm', executable='perception_node', output='screen')
    skills     = Node(package='panda_vlm', executable='skills_server', output='screen')

    return LaunchDescription([base, cam_bridge, perception, skills])
