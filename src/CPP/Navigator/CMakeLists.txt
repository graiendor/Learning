#cmake_minimum_required(VERSION 3.23)
#project(Graph)
#
#
#set(CMAKE_CXX_STANDARD 17)
#
#INCLUDE_DIRECTORIES(libs)
#LINK_DIRECTORIES(libs)
#
#file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/Graph/graph.txt
#        DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
#
#file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/GraphAlgorithms/test1.txt
#        DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
#
#file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/GraphAlgorithms/test2.txt
#        DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
#
#add_executable(Graph
#        Graph/test_graph.cpp
#        Graph/graph.cpp Graph/graph.h)
#
#add_executable(GraphAlgorithms
#        Graph/graph.cpp Graph/graph.h
#        GraphAlgorithms/test_graph_algorithms.cpp
#        GraphAlgorithms/GraphAlgorithms.cpp GraphAlgorithms/GraphAlgorithms.h)
#
#add_executable(Start
#        Interface/Interface.cpp)

cmake_minimum_required (VERSION 3.23)

# --- Fetch FTXUI --------------------------------------------------------------
include(FetchContent)

set(FETCHCONTENT_UPDATES_DISCONNECTED TRUE)
FetchContent_Declare(ftxui
        GIT_REPOSITORY https://github.com/ArthurSonzogni/ftxui
        # Important: Specify a GIT_TAG XXXXX here.
        )

FetchContent_GetProperties(ftxui)
if(NOT ftxui_POPULATED)
    FetchContent_Populate(ftxui)
    add_subdirectory(${ftxui_SOURCE_DIR} ${ftxui_BINARY_DIR} EXCLUDE_FROM_ALL)
endif()

# ------------------------------------------------------------------------------

project(simpleNavigator
        LANGUAGES CXX
        VERSION 1.0.0
        )

add_executable(simpleNavigator
        Interface/Interface.cpp Interface/Interface.h
        Graph/graph.cpp Graph/graph.h
        GraphAlgorithms/GraphAlgorithms.cpp GraphAlgorithms/GraphAlgorithms.h)

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/Graph/graph.txt
        DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/GraphAlgorithms/test1.txt
        DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/GraphAlgorithms/test2.txt
        DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
#target_include_directories(ftxui-starter PRIVATE src)

target_link_libraries(simpleNavigator
        PRIVATE ftxui::screen
        PRIVATE ftxui::dom
        PRIVATE ftxui::component # Not needed for this example.
        )