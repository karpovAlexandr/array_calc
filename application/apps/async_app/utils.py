from uuid import uuid4


def generate_str_uuid() -> str:
    return uuid4().__str__()
