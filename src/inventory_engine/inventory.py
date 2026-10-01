from .exceptions import (
    DuplicateProductError,
    InsufficientStockError,
    ProductNotFoundError,
)


class Inventory:
    """Manage products and stock."""

    def __init__(self):
        self._products = {}

    def add_product(self, product):
        """Add a product to the inventory."""

        if product.product_id in self._products:
            raise DuplicateProductError(
                f"Product '{product.product_id}' already exists."
            )

        self._products[product.product_id] = product

    def get_product(self, product_id):
        """Return a product by ID."""

        if product_id not in self._products:
            raise ProductNotFoundError(
                f"Product '{product_id}' was not found."
            )

        return self._products[product_id]

    def remove_product(self, product_id):
        """Remove a product."""

        if product_id not in self._products:
            raise ProductNotFoundError(
                f"Product '{product_id}' was not found."
            )

        del self._products[product_id]

    def list_products(self):
        """Return all products."""

        return list(self._products.values())

    def restock(self, product_id, quantity):
        """Increase product stock."""

        product = self.get_product(product_id)

        if quantity <= 0:
            raise ValueError(
                "Restock quantity must be positive."
            )

        product.quantity += quantity

    def sell(self, product_id, quantity):
        """Decrease product stock."""

        product = self.get_product(product_id)

        if quantity <= 0:
            raise ValueError(
                "Sale quantity must be positive."
            )

        if quantity > product.quantity:
            raise InsufficientStockError(
                f"Not enough stock for '{product_id}'."
            )

        product.quantity -= quantity