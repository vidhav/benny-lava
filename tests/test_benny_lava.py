from benny_lava import get_quote, get_value


def test_get_quote():
    quote = get_quote()
    assert quote == "The Ninja made a Movement"


def test_get_value():
    res = get_value(42)
    assert res["id"] == 42
    assert res["value"] >= 10 and res["value"] <= 99
