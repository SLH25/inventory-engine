from abc import ABC, abstractmethod

from .exceptions import InvalidProductError


class Product(ABC):
    """Base class representing a product."""

    def __init__(self, product_id, name, price, quantity):
        self._product_id = product_id
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def product_id(self):
        """Return the product ID."""
        return self._product_id

    @property
    def name(self):
        """Return the product name."""
        return self._name

    @property
    def price(self):
        """Return the product price."""
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise InvalidProductError(
                "Price cannot be negative."
            )

        self._price = float(value)

    @property
    def quantity(self):
        """Return the available quantity."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise InvalidProductError(
                "Quantity cannot be negative."
            )

        self._quantity = int(value)

    @property
    @abstractmethod
    def product_type(self):
        """Return the product type."""
        pass

    @abstractmethod
    def description(self):
        """Return a product description."""
        pass

    def to_dict(self):
        """Convert the product into a dictionary."""

        return {
            "id": self.product_id,
            "type": self.product_type,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
        }


class PhysicalProduct(Product):
    """Product that exists physically."""

    @property
    def product_type(self):
        return "physical"

    def description(self):
        return (
            f"Physical product: {self.name} "
            f"(${self.price:.2f})"
        )


class PerishableProduct(PhysicalProduct):
    """Physical product with an expiration date."""

    def __init__(
        self,
        product_id,
        name,
        price,
        quantity,
        expiration_date,
    ):
        super().__init__(
            product_id,
            name,
            price,
            quantity,
        )

        if not expiration_date:
            raise InvalidProductError(
                "Expiration date is required."
            )

        self._expiration_date = expiration_date

    @property
    def expiration_date(self):
        return self._expiration_date

    @property
    def product_type(self):
        return "perishable"

    def description(self):
        return (
            f"Perishable product: {self.name} "
            f"(${self.price:.2f}) "
            f"- expires {self.expiration_date}"
        )

    def to_dict(self):
        data = super().to_dict()
        data["expiration_date"] = self.expiration_date
        return data


class DigitalProduct(Product):
    """Product delivered digitally."""

    def __init__(
        self,
        product_id,
        name,
        price,
        quantity,
        download_url,
    ):
        super().__init__(
            product_id,
            name,
            price,
            quantity,
        )

        if not download_url:
            raise InvalidProductError(
                "Download URL is required."
            )

        self._download_url = download_url

    @property
    def download_url(self):
        return self._download_url

    @property
    def product_type(self):
        return "digital"

    def description(self):
        return (
            f"Digital product: {self.name} "
            f"(${self.price:.2f})"
        )

    def to_dict(self):
        data = super().to_dict()
        data["download_url"] = self.download_url
        return data