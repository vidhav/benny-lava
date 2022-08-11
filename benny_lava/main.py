from random import randint


def get_quote() -> str:
    return "The Ninja made a Movement"


def get_value(id_: int) -> str:
    return {
        "id": id_,
        "value": randint(10, 99),
    }
