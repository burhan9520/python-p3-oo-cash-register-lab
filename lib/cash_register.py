class CashRegister:
    def __init__(self):
        self.items = []
        self.total = 0.0

    def add_item(self, item_name, item_price, quantity=1):
        self.items.extend([(item_name, item_price, quantity)])
        self.total += item_price * quantity

    def void_last_transaction(self):
        if self.items:
            _, last_item_price, last_item_quantity = self.items.pop()
            self.total -= last_item_price * last_item_quantity

    pass
