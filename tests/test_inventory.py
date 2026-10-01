import unittest

from inventory_engine.exceptions import (
    DuplicateProductError,
    InsufficientStockError,
    ProductNotFoundError,
)
from inventory_engine.inventory import Inventory
from inventory_engine.models import PhysicalProduct


class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()

        self.product = PhysicalProduct(
            "P001",
            "Laptop",
            800,
            10,
        )

    def test_add_product(self):
        self.inventory.add_product(self.product)

        result = self.inventory.get_product("P001")

        self.assertEqual(result.name, "Laptop")

    def test_duplicate_product(self):
        self.inventory.add_product(self.product)

        with self.assertRaises(DuplicateProductError):
            self.inventory.add_product(self.product)

    def test_product_not_found(self):
        with self.assertRaises(ProductNotFoundError):
            self.inventory.get_product("UNKNOWN")

    def test_remove_product(self):
        self.inventory.add_product(self.product)

        self.inventory.remove_product("P001")

        with self.assertRaises(ProductNotFoundError):
            self.inventory.get_product("P001")

    def test_restock(self):
        self.inventory.add_product(self.product)

        self.inventory.restock("P001", 5)

        product = self.inventory.get_product("P001")

        self.assertEqual(product.quantity, 15)

    def test_sell(self):
        self.inventory.add_product(self.product)

        self.inventory.sell("P001", 3)

        product = self.inventory.get_product("P001")

        self.assertEqual(product.quantity, 7)

    def test_insufficient_stock(self):
        self.inventory.add_product(self.product)

        with self.assertRaises(InsufficientStockError):
            self.inventory.sell("P001", 20)


if __name__ == "__main__":
    unittest.main()