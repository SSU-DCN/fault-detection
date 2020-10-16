# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service_pb2 as service__pb2


class MonitorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NewTargetRequest = channel.unary_unary(
                '/Monitor/NewTargetRequest',
                request_serializer=service__pb2.MonitorRequest.SerializeToString,
                response_deserializer=service__pb2.MonitorReply.FromString,
                )
        self.DelTargetRequest = channel.unary_unary(
                '/Monitor/DelTargetRequest',
                request_serializer=service__pb2.VnfId.SerializeToString,
                response_deserializer=service__pb2.MonitorReply.FromString,
                )


class MonitorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NewTargetRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelTargetRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NewTargetRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.NewTargetRequest,
                    request_deserializer=service__pb2.MonitorRequest.FromString,
                    response_serializer=service__pb2.MonitorReply.SerializeToString,
            ),
            'DelTargetRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.DelTargetRequest,
                    request_deserializer=service__pb2.VnfId.FromString,
                    response_serializer=service__pb2.MonitorReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Monitor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Monitor(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NewTargetRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Monitor/NewTargetRequest',
            service__pb2.MonitorRequest.SerializeToString,
            service__pb2.MonitorReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelTargetRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Monitor/DelTargetRequest',
            service__pb2.VnfId.SerializeToString,
            service__pb2.MonitorReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
