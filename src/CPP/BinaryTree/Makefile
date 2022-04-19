all: build

build:
	g++ BinaryTree.cpp -lgtest -o testBin
	./testBin
	-CK_FORK=no leaks --atExit -- ./testBin > res.txt || echo "LEAKS!!! = $$?"