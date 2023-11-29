import math
import pytest
from cash_register import CashRegister

@pytest.fixture
def cash_register():
    return CashRegister()

class TestCashRegister:
    def test_add_item_optional_quantity(self, cash_register):
        cash_register.add_item("book", 5.00, 3)
        assert math.isclose(cash_register.total, 5.00 * 3, rel_tol=1e-2)

    def test_void_last_transaction_with_multiples(self, cash_register):
        cash_register.add_item("tomato", 1.76, 2)
        cash_register.void_last_transaction()
        assert math.isclose(cash_register.total, 0.0, rel_tol=1e-2)

    def test_items_list_without_multiples(self, cash_register):
        new_register = CashRegister()
        new_register.add_item("eggs", 1.99)
        new_register.add_item("tomato", 1.76)
        expected_items = ["eggs", "tomato"]
        actual_items = [item[0] for item in new_register.items]
        assert set(actual_items) == set(expected_items)

    def test_items_list_with_multiples(self, cash_register):
        new_register = CashRegister()
        new_register.add_item("eggs", 1.99, 2)
        new_register.add_item("tomato", 1.76, 3)
        expected_items = ["eggs", "eggs", "tomato", "tomato", "tomato"]
        actual_items = [item[0] for item in new_register.items]
        assert set(actual_items) == set(expected_items)













      