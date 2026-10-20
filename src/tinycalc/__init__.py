"""Tiny calculator library."""

__all__ = ["add", "subtract", "multiply", "divide"]


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float | None:
    """Return the quotient of a and b, or None when b is zero."""
    if b == 0:
        return None
    return a / b
