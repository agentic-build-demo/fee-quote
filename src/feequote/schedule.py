"""The fee schedule interface. A schedule knows each tier's rate and the minimum fee."""

from decimal import Decimal
from typing import Protocol, runtime_checkable


class UnknownTier(KeyError):
    """The schedule has no rate for this tier."""


@runtime_checkable
class FeeSchedule(Protocol):
    """Any object with a minimum fee and a rate per tier, in basis points."""

    minimum_fee: Decimal

    def rate_bps(self, tier: str) -> int:
        """Return the tier's rate in basis points. Raise UnknownTier for an unknown tier."""
        ...
