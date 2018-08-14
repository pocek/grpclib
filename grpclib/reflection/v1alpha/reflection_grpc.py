# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: grpclib/reflection/v1alpha/reflection.proto
# plugin: grpclib.plugin.main
import abc

import grpclib.const
import grpclib.client

import grpclib.reflection.v1alpha.reflection_pb2


class ServerReflectionBase(abc.ABC):

    @abc.abstractmethod
    async def ServerReflectionInfo(self, stream):
        pass

    def __mapping__(self):
        return {
            '/grpc.reflection.v1alpha.ServerReflection/ServerReflectionInfo': grpclib.const.Handler(
                self.ServerReflectionInfo,
                grpclib.const.Cardinality.STREAM_STREAM,
                grpclib.reflection.v1alpha.reflection_pb2.ServerReflectionRequest,
                grpclib.reflection.v1alpha.reflection_pb2.ServerReflectionResponse,
            ),
        }


class ServerReflectionStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ServerReflectionInfo = grpclib.client.StreamStreamMethod(
            channel,
            '/grpc.reflection.v1alpha.ServerReflection/ServerReflectionInfo',
            grpclib.reflection.v1alpha.reflection_pb2.ServerReflectionRequest,
            grpclib.reflection.v1alpha.reflection_pb2.ServerReflectionResponse,
        )