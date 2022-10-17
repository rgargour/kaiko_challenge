# Requirements

- make
- python 3.6 or higher
- python libraries: `grpcio` and `grpcio-tools`

# Build
Once the requirements are installed, just run `make generate-artifacts`, it will generate `kaiko_pb2.py` and `kaiko_pb2_grpc.py` . 

# How to run the server
Run `make run-server`, then you can run your client commands in another window.

# How to test the server
Run `make run-integration-tests`. The tests implemented are the tests mentioned in the client' readme.