class InventoryError(Exception):
    """Base exception for inventory errors."""


class InvalidProductError(InventoryError):
    """Raised when product data is invalid."""


class ProductNotFoundError(InventoryError):
    """Raised when a product cannot be found."""


class DuplicateProductError(InventoryError):
    """Raised when a product ID already exists."""


class InsufficientStockError(InventoryError):
    """Raised when there is not enough stock."""