#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """Initializes the cash register with an optional discount"""
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        """Adds an item to the register with its price and quantity"""
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        """Applies the discount to the total price"""
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f'After the discount, the total comes to ${self.total:.0f}.')
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
        """Reverts the last transaction"""
        if self.last_transaction is not None:
            self.total -= self.last_transaction
            self.last_transaction = None
            
            if self.items:
                
                for i in reversed(range(len(self.items))):
                    if self.total == self.last_transaction:
                        self.items.pop(i)
                        break
            
            if not self.items:
                self.total = 0
