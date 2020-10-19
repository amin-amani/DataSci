# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ImageTransfer_pb2 as ImageTransfer__pb2


class ImageProcedureStub(object):
    """service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ImageMeanWH = channel.unary_unary(
                '/ImageProcedure/ImageMeanWH',
                request_serializer=ImageTransfer__pb2.B64Image.SerializeToString,
                response_deserializer=ImageTransfer__pb2.Prediction.FromString,
                )


class ImageProcedureServicer(object):
    """service
    """

    def ImageMeanWH(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageProcedureServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ImageMeanWH': grpc.unary_unary_rpc_method_handler(
                    servicer.ImageMeanWH,
                    request_deserializer=ImageTransfer__pb2.B64Image.FromString,
                    response_serializer=ImageTransfer__pb2.Prediction.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImageProcedure', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageProcedure(object):
    """service
    """

    @staticmethod
    def ImageMeanWH(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImageProcedure/ImageMeanWH',
            ImageTransfer__pb2.B64Image.SerializeToString,
            ImageTransfer__pb2.Prediction.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
