from typing import Dict


def encode_data(pb_cls, d: Dict):
    protobuf_message = pb_cls(**d)
    encoded_data = protobuf_message.SerializeToString()
    return encoded_data
