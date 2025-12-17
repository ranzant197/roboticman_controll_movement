import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math


class SimpleJointController(Node):
    def __init__(self):
        super().__init__('simple_joint_controller')

        self.publisher_ = self.create_publisher(
            JointState,
            '/joint_states',
            10
        )

        self.timer = self.create_timer(0.02, self.timer_callback)
        self.start_time = self.get_clock().now()

        self.joint_names = [
            'body_to_head',
            'body_to_right_arm',
            'body_to_left_arm',
            'right_arm_right_fingure',
            'left_arm_left_fingure',
            'hips_to_left_leg',
            'hips_to_right_leg'
        ]

    def timer_callback(self):
        now = self.get_clock().now()
        t = (now - self.start_time).nanoseconds * 1e-9

        msg = JointState()
        msg.header.stamp = now.to_msg()
        msg.name = self.joint_names

        hip_motion = 0.5 * math.sin(2 * t)
        head_motion = 0.3 * math.sin(2 * t)
        arm_motion = 0.6 * math.sin(2 * t)

        msg.position = [
            head_motion,            # head
            -arm_motion,            # right arm
            -arm_motion,            # left arm
            0.0,            # right finger
            0.0,            # left finger
            hip_motion,     # left leg
            hip_motion     # right leg
        ]

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = SimpleJointController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
