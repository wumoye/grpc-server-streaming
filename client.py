# coding:utf-8

import grpc
import data_pb2 as pb2
import data_pb2_grpc as pb2_grpc


_HOST = 'localhost'
_PORT = '8006'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = pb2_grpc.TestClientRecvStub(channel=conn)
    resposne = client.TestClientRecvStream(pb2.TestClientRecvStreamRequest(
        data='close'
    ))

    for item in resposne:
        print(item.result)


if __name__ == '__main__':
    run()
