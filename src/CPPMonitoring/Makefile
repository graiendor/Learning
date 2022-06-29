all: build

build:
	g++ -std=c++17 Model/CPU_agent/CPU_agent.cpp Tests/test_CPU.cpp -o agents/CPU_agent
	agents/CPU_agent

memory:
	g++ -std=c++17 Model/MEM_agent/MEM_agent.cpp Tests/test_MEM.cpp -o agents/MEM_agent
	agents/MEM_agent

net:
	g++ -std=c++17 Model/NET_agent/NET_agent.cpp Tests/test_NET.cpp -o agents/NET_agent
	agents/NET_agent