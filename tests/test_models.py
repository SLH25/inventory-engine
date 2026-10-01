import unittest

from inventory_engine.exceptions import InvalidProductError
from inventory_engine.models import (
    DigitalProduct,
    PerishableProduct,
    PhysicalProduct,
)


class TestProducts(unittest.TestCase):

    def test_physical_product(self):
        product = PhysicalProduct(
            "P001",
            "Laptop",
            800,
            10,
        )

        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 800)
        self.assertEqual(product.quantity, 10)

    def test_perishable_product(self):
        product = PerishableProduct(
            "P002",
            "Milk",
            2.5,
            20,
            "2026-10-10",
        )

        self.assertEqual(
            product.product_type,
            "perishable",
        )

        self.assertIn(
            "expires 2026-10-10",
            product.description(),
        )

    def test_digital_product(self):
        product = DigitalProduct(
            "P003",
            "Python Course",
            50,
            100,
            "https://example.com/course",
        )

        self.assertEqual(
            product.product_type,
            "digital",
        )

        self.assertIn(
            "Digital product",
            product.description(),
        )

    def test_negative_price(self):
        with self.assertRaises(InvalidProductError):
            PhysicalProduct(
                "P004",
                "Phone",
                -100,
                5,
            )

    def test_negative_quantity(self):
        with self.assertRaises(InvalidProductError):
            PhysicalProduct(
                "P005",
                "Mouse",
                20,
                -5,
            )


if __name__ == "__main__":
    unittest.main()