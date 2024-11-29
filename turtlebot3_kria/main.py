import rclpy

from turtlebot3_kria import Turtlebot3Kria


def main(args=None):
    rclpy.init(args=args)
    turtlebot3_kria_control = Turtlebot3Kria()
    rclpy.spin(turtlebot3_kria_control)

    turtlebot3_kria_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
