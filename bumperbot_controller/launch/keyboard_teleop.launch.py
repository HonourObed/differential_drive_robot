from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    keyboard_teleop_node = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_twist_keyboard_node',
        output='screen',
        # THIS IS THE TRICK: Open in a new xterm window
        prefix='xterm -e',
        
        # REMAPPING: Connect the keyboard directly to your controller
        remappings=[
            ('/cmd_vel', '/bumperbot_controller/cmd_vel'),
        ]
    )

    return LaunchDescription([
        keyboard_teleop_node
    ])