import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from fastapi import FastAPI
import threading

# Crear la app de FastAPI
app = FastAPI()

# Nodo ROS que publicará en el tópico 'robot_command'
class ROSPublisherNode(Node):
    def __init__(self):
        super().__init__('api_publisher')
        self.publisher_ = self.create_publisher(String, 'robot_command', 10)

    def publish_command(self, command):
        msg = String()
        msg.data = command
        self.publisher_.publish(msg)
        self.get_logger().info(f'📤 Sent command: {command}')

# Inicializa ROS 2 y el nodo en un hilo aparte
rclpy.init()
ros_node = ROSPublisherNode()

def ros_spin():
    rclpy.spin(ros_node)

# Lanza el spin en segundo plano
threading.Thread(target=ros_spin, daemon=True).start()

# Endpoints de la API
@app.get("/start")
def start_robot():
    ros_node.publish_command("start")
    return {"status": "started"}

@app.get("/stop")
def stop_robot():
    ros_node.publish_command("stop")
    return {"status": "stopped"}

@app.get("/status")
def status_robot():
    ros_node.publish_command("status")
    return {"status": "queried"}

def main():
    import uvicorn
    uvicorn.run("py_talker_listener.ros_api_server:app", host="0.0.0.0", port=8000, reload=False)
