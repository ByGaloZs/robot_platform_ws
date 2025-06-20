from setuptools import setup
import os
from glob import glob

package_name = 'py_talker_listener'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        # 👇 Añade esta línea para incluir archivos .srv
        (os.path.join('share', package_name, 'srv'), glob('srv/*.srv')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mario',
    maintainer_email='mario@example.com',
    description='Python ROS 2 pub-sub and services demo',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_talker_listener.publisher_node:main',
            'listener = py_talker_listener.subscriber_node:main',
            'ros_api_server = py_talker_listener.ros_api_server:main',
        ],
    },
)
