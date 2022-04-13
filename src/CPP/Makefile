all: build

build: clean
	g++ TestSuffixTree.cpp -lgtest -o testSuf
	./testSuf
	-CK_FORK=no leaks --atExit -- ./testSuf > res.txt || echo "LEAKS!!! = $$?"
#	g++ ExponentialSearch.cpp -lgtest -o testExp
#	./testExp
#    -CK_FORK=no leaks --atExit -- ./testExp > res.txt || echo "LEAKS!!! = $$?"

clean:
	rm -rf test*