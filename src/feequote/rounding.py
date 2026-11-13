"""Fee arithmetic."""

from decimal import Decimal


def compute_fee(amount: Decimal, rate_bps: int, minimum_fee: Decimal) -> Decimal:
    """Return the fee for an amount: amount times rate, rounded half up to cents, never below the minimum."""
    raise NotImplementedError("compute_fee is not built yet")
