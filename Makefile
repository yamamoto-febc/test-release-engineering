.PHONY: clean
clean:
	rm -Rf bin/*

build:
	go build -o bin/test-release-engineering main.go

