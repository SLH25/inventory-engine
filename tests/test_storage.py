import tempfile
import unittest
from pathlib import Path

from inventory_engine.models import (
    DigitalProduct,
    PerishableProduct,
)
from inventory_engine.storage import InventoryStorage


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.products = [
            PerishableProduct(
                "P001",
                "Milk",
                2.5,
                20,
                "2026-10-10",
            ),
            DigitalProduct(
                "P002",
                "Python Course",
                50,
                100,
                "https://example.com/course",
            ),
        ]

    def test_json_storage(self):
        with tempfile.TemporaryDirectory() as directory:

            path = Path(directory) / "products.json"

            InventoryStorage.save_json(
                self.products,
                path,
            )

            loaded = InventoryStorage.load_json(path)

            self.assertEqual(len(loaded), 2)
            self.assertEqual(
                loaded[0].name,
                "Milk",
            )
            self.assertEqual(
                loaded[1].name,
                "Python Course",
            )

    def test_csv_storage(self):
        with tempfile.TemporaryDirectory() as directory:

            path = Path(directory) / "products.csv"

            InventoryStorage.save_csv(
                self.products,
                path,
            )

            loaded = InventoryStorage.load_csv(path)

            self.assertEqual(len(loaded), 2)
            self.assertEqual(
                loaded[0].name,
                "Milk",
            )
            self.assertEqual(
                loaded[1].name,
                "Python Course",
            )


if __name__ == "__main__":
    unittest.main()