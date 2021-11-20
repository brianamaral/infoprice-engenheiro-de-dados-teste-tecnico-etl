def is_status_ok(response: dict) -> bool:
    if response["status"] != "OK":
        return "NOT OK"
    else:
        return "OK"


def cast_to_int(element) -> int:
    return int(element)


def get_name(response: dict) -> str:
    return response["nome"]


def get_city(response: dict) -> str:
    return response["gepirParty"]["partyDataLine"]["address"]["city"]


def get_state(response: dict) -> str:
    return response["gepirParty"]["partyDataLine"]["address"]["state"]
