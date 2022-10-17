from concurrent import futures
import logging
import requests
import json

import grpc
import kaiko_pb2
import kaiko_pb2_grpc


class KaikoServicer(kaiko_pb2_grpc.KaikoServicer):
    def __init__(self):
        pass

    def Exists(self, request, context):
        exchange_code = request.exchange_code
        exchange_pair_code = request.exchange_pair_code
        response = requests.request(
            "GET",
            f"https://reference-data-api.kaiko.io/v1/instruments/?exchange_code={exchange_code}",
        )
        response_json = json.loads(response.text)
        if response_json["count"] == 0:
            res = kaiko_pb2.ExistsResponse()
            res.exists = kaiko_pb2.ExistsResponse.UNKNOWN
            return res
        # please note that exchange_pair_code={exchange_pair_code} is not working in the url
        # after analysing data, I noticed that exchange_pair_code = quote_asset + '-' + base_asset
        # we can eventually use this relationship to call the API but not sure that it's faster than the solution implemented
        # since we call the network, which can be slow
        else:
            data = response_json["data"]
            for elt in data:
                # Since a pair of coins is not case-sensitive (BTC is bitcoin and btc is bitcoin too)
                if elt["exchange_pair_code"].lower() == exchange_pair_code.lower():
                    res = kaiko_pb2.ExistsResponse()
                    res.exists = kaiko_pb2.ExistsResponse.YES
                    return res
        res = kaiko_pb2.ExistsResponse()
        res.exists = kaiko_pb2.ExistsResponse.NO
        return res


def serve():
    # the adress of the server is localhost, the port is 8080
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kaiko_pb2_grpc.add_KaikoServicer_to_server(KaikoServicer(), server)
    server.add_insecure_port("[::]:8080")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
