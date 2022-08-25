cmake_minimum_required(VERSION 3.23)
project(Graph)


set(CMAKE_CXX_STANDARD 17)

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/Graph/graph.txt
        DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/GraphAlgorithms/test1.txt
        DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

add_executable(Graph
        Graph/test_graph.cpp
        Graph/graph.cpp Graph/graph.h)

add_executable(GraphAlgorithms
        Graph/graph.cpp Graph/graph.h
        GraphAlgorithms/test_graph_algorithms.cpp
        GraphAlgorithms/GraphAlgorithms.cpp GraphAlgorithms/GraphAlgorithms.h)

