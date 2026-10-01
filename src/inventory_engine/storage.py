import csv
import json
from pathlib import Path

from .models import (
    DigitalProduct,
    PerishableProduct,
    PhysicalProduct,
)


class InventoryStorage:
    """Handle JSON and CSV persistence."""

    @staticmethod
    def save_json(products, file_path):
        """Save products to JSON."""

        path = Path(file_path)

        data = [
            product.to_dict()
            for product in products
        ]

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=2,
            )

    @staticmethod
    def load_json(file_path):
        """Load products from JSON."""

        path = Path(file_path)

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        return [
            InventoryStorage._create_product(item)
            for item in data
        ]

    @staticmethod
    def save_csv(products, file_path):
        """Save products to CSV."""

        path = Path(file_path)

        fieldnames = [
            "id",
            "type",
            "name",
            "price",
            "quantity",
            "expiration_date",
            "download_url",
        ]

        with path.open(
            "w",
            encoding="utf-8",
            newline="",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
            )

            writer.writeheader()

            for product in products:
                data = product.to_dict()

                row = {
                    field: data.get(field, "")
                    for field in fieldnames
                }

                writer.writerow(row)

    @staticmethod
    def load_csv(file_path):
        """Load products from CSV."""

        path = Path(file_path)

        products = []

        with path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                data = {
                    "id": row["id"],
                    "type": row["type"],
                    "name": row["name"],
                    "price": float(row["price"]),
                    "quantity": int(row["quantity"]),
                }

                if row.get("expiration_date"):
                    data["expiration_date"] = (
                        row["expiration_date"]
                    )

                if row.get("download_url"):
                    data["download_url"] = (
                        row["download_url"]
                    )

                products.append(
                    InventoryStorage._create_product(data)
                )

        return products

    @staticmethod
    def _create_product(data):
        """Create the appropriate product subclass."""

        product_type = data["type"]

        if product_type == "physical":
            return PhysicalProduct(
                data["id"],
                data["name"],
                data["price"],
                data["quantity"],
            )

        if product_type == "perishable":
            return PerishableProduct(
                data["id"],
                data["name"],
                data["price"],
                data["quantity"],
                data["expiration_date"],
            )

        if product_type == "digital":
            return DigitalProduct(
                data["id"],
                data["name"],
                data["price"],
                data["quantity"],
                data["download_url"],
            )

        raise ValueError(
            f"Unknown product type: {product_type}"
        )