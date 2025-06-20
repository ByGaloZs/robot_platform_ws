cmake_minimum_required(VERSION 3.8)
project(py_talker_listener)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Encuentra dependencias
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# Instalación
install(
  DIRECTORY py_talker_listener
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
