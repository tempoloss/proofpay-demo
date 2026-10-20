"""Tiny calculator library."""

__all__ = ["add", "subtract", "multiply", "divide", "percent"]


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a and b."""
    return a / b


def percent(part: float, whole: float) -> float:
    """Return part as a percentage of whole."""
    return part / whole * 100
