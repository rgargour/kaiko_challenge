.PHONY: build-image
build-image:
	docker build -t kaiko-grpc .

.PHONY: run-docker-image
run-docker-image:
	docker run -p 127.0.0.1:8080:8080 kaiko-grpc