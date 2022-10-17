import grpc
import kaiko_pb2_grpc
import kaiko_pb2
import pytest

@pytest.mark.parametrize(
    "exchange_code,exchange_pair_code,expected",
    [
        pytest.param(
            "cbse", "btc-usd", kaiko_pb2.ExistsResponse.YES
        ),
        pytest.param(
            "cbse", "foo-bar", kaiko_pb2.ExistsResponse.NO
        ),
        pytest.param(
            "foo", "foo-bar", kaiko_pb2.ExistsResponse.UNKNOWN
        ),
    ],
)
def test_verify_responses(exchange_code, exchange_pair_code, expected):
    channel = grpc.insecure_channel('localhost:8080')
    stub = kaiko_pb2_grpc.KaikoStub(channel)
    exchange_info = kaiko_pb2.ExistsRequest(
        exchange_code=exchange_code,
        exchange_pair_code=exchange_pair_code)
    exists = stub.Exists(exchange_info)
    expected_exists = kaiko_pb2.ExistsResponse()
    expected_exists.exists = expected
    assert exists == expected_exists

