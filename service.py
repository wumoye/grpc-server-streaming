# coding:utf-8

import time

import grpc
import data_pb2 as pb2
import data_pb2_grpc as pb2_grpc

from concurrent import futures

_HOST = 'localhost'
_PORT = '8006'

class TestClientRecv(pb2_grpc.TestClientRecvServicer):
    def TestClientRecvStream(self, request, context):
        index = 0
        while context.is_active():
            data = request.data

            if data == 'close':
                print('data is close,request will cancel')
                context.cancel()

            time.sleep(1)
            index += 1
            result = 'send %d %s' % (index, data)
            print(result)
            yield pb2.TestClientRecvStreamResponse(
                result=result
            )


def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    pb2_grpc.add_TestClientRecvServicer_to_server(TestClientRecv(), grpc_server)
    grpc_server.add_insecure_port(_HOST + ':' + _PORT)
    print(f'server will start at {_HOST}:{_PORT}')
    grpc_server.start()

    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    run()
