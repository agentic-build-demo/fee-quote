"""Fee arithmetic."""

from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")
BPS_PER_UNIT = Decimal(10000)


def compute_fee(amount: Decimal, rate_bps: int, minimum_fee: Decimal) -> Decimal:
    """Return the fee for an amount: amount times rate, rounded half up to cents, never below the minimum."""
    fee = (amount * Decimal(rate_bps) / BPS_PER_UNIT).quantize(CENT, rounding=ROUND_HALF_UP)
    return max(fee, minimum_fee)
