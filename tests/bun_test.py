import pytest
from praktikum.bun import Bun
from tests.data import BUNS_DATA


class TestBun:
    @pytest.mark.parametrize("bun_data", BUNS_DATA)
    def test_bun_creation_get_name_returns_correct_name(self, bun_data):
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_name() == bun_data["name"]

    @pytest.mark.parametrize("bun_data", BUNS_DATA)
    def test_bun_creation_get_price_returns_correct_price(self, bun_data):
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_price() == bun_data["price"]

    def test_bun_different_objects_different_memory_addresses(self, real_bun_black, real_bun_white):
        assert id(real_bun_black) != id(real_bun_white)

    def test_bun_get_name_returns_string_type(self, real_bun_black):
        result = real_bun_black.get_name()
        assert isinstance(result, str)