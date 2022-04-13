all: build

build: clean
	g++ ExponentialSearch.cpp TestExponentialSearch.cpp -o testExp
	./testExp
    -CK_FORK=no leaks --atExit -- ./testExp > res.txt || echo "LEAKS!!! = $$?"

clean:
	rm -rf test*