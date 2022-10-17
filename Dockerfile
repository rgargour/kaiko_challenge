# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

RUN python -m pip install grpcio grpcio-tools requests
COPY . /usr/local/grpc-poc

RUN cd usr/local/grpc-poc/server \
    && python -m grpc_tools.protoc -I../ --python_out=. --grpc_python_out=. ../kaiko.proto
# to open the port in the container
EXPOSE 8080

# default command ran when we run the docker image
ENTRYPOINT ["python", "usr/local/grpc-poc/server/kaiko_server.py"]