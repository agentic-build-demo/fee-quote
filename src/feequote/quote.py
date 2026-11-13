"""The Quote type: the result of quoting a fee (PBI decision D3)."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Quote:
    """One fee quote. Money fields are Decimal (decision D1)."""

    amount: Decimal
    tier: str
    rate_bps: int
    fee: Decimal
    net: Decimal

    def __post_init__(self) -> None:
        for name in ("amount", "fee", "net"):
            if not isinstance(getattr(self, name), Decimal):
                raise TypeError(f"{name} must be a Decimal")
        if self.net != self.amount - self.fee:
            raise ValueError("net must equal amount minus fee")
