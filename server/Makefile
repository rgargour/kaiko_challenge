ARTIFACTS=
ARTIFACTS += kaiko_pb2.py
ARTIFACTS += kaiko_pb2_grpc.py

.PHONY: run-server
run-server:
	python kaiko_server.py

.PHONY: run-integration-tests
run-integration-tests:
	pytest server_test.py

.PHONY: clean
clean:
	rm -f ${ARTIFACTS}

.PHONY: generate-artifacts
generate-artifacts: ${ARTIFACTS}

kaiko_pb2.py kaiko_pb2_grpc.py : ../kaiko.proto
	python -m grpc_tools.protoc -I../ --python_out=. --grpc_python_out=. ../kaiko.proto

