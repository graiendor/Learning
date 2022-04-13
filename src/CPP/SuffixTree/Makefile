all: build

build: clean
	g++ TestSuffixTree.cpp SuffixTree.cpp -lgtest -o testSuf
	./testSuf
	-CK_FORK=no leaks --atExit -- ./testSuf > res.txt || echo "LEAKS!!! = $$?"

clean:
	rm -rf test*