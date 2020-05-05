import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridge, CvBridgeError

class Image_Publisher(Node):
    def __init__(self):
        super().__init__("image_tutorial")
        self.add_msg_to_info_logger("initializing node")
        self.image_publisher_ = self.create_publisher(Image, 'image', 1)
        self.bridge = CvBridge()

        
    def publish(self, cv2_image):
        self.add_msg_to_info_logger("sending_image")
        try:
             msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
             self.publisher_.publish(msg)
        except CvBridgeError as e:
             self.add_msg_to_info_logger(e)
        

    def add_msg_to_info_logger(self, msg):
        self.get_logger().info(msg)
        

rclpy.init(None)
image_publisher = Image_Publisher()

image_publisher.add_msg_to_info_logger("initializing camera")
cam = cv2.VideoCapture(0)
cv2.namedWindow("image_tutorial")

while True:
    ret, frame = cam.read()
    if not ret:
        image_publisher.add_msg_to_info_logger("something went wrong. camera is offline?")
        break
        
    cv2.imshow("image_tutorial", frame)
    pressed = cv2.waitKey(1)
    if pressed == chr(27).encode() or pressed == ord('q'):
        # closing application if esc or q pressed
        image_publisher.add_msg_to_info_logger("closing button pressed, closing")
        break
        
    elif pressed == chr(32).encode():
        # publishing image if space pressed
        image_publisher.publish(frame)

# closing  
image_publisher.destroy_node()
rclpy.shutdown()   
cam.release()
cv2.destroyAllWindows()
