"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _TransportType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TransportTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TransportType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TELEPORT: _TransportType.ValueType  # 0
    WALK: _TransportType.ValueType  # 1

class TransportType(_TransportType, metaclass=_TransportTypeEnumTypeWrapper): ...

TELEPORT: TransportType.ValueType  # 0
WALK: TransportType.ValueType  # 1
global___TransportType = TransportType
