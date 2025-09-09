cmake_minimum_required(VERSION 3.16)
project(mmn14-server VERSION 1.0 LANGUAGES CXX)

# Set C++ standard to C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include directories
include_directories(${CMAKE_SOURCE_DIR}/include)

# Source files
file(GLOB_RECURSE SOURCES ${CMAKE_SOURCE_DIR}/src/*.cpp)

# Explicitly add important source files (to avoid linker issues if glob misses them)
set(SOURCES
    ${SOURCES}
    ${CMAKE_SOURCE_DIR}/src/Server.cpp
    ${CMAKE_SOURCE_DIR}/src/RequestHandler.cpp
)

# Set the output directory for the executable
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build)

# Create executable
add_executable(${PROJECT_NAME} ${SOURCES})

# Boost (asio, system, etc.)
find_package(Boost REQUIRED COMPONENTS system)
include_directories(${Boost_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} ${Boost_LIBRARIES})
