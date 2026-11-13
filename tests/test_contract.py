"""Criterion 1: the Quote type and the schedule interface."""

from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest

from feequote import FeeSchedule, Quote, UnknownTier


def make_quote(**changes):
    fields = dict(amount=Decimal("1000.00"), tier="gold", rate_bps=25, fee=Decimal("2.50"), net=Decimal("997.50"))
    fields.update(changes)
    return Quote(**fields)


# A quote keeps the five fields from decision D3, with money as Decimal.
def test_quote_has_the_five_fields():
    q = make_quote()
    assert (q.amount, q.tier, q.rate_bps, q.fee, q.net) == (
        Decimal("1000.00"), "gold", 25, Decimal("2.50"), Decimal("997.50"))


# A float in a money field is refused, because floats lose cents.
@pytest.mark.parametrize("field", ["amount", "fee", "net"])
def test_quote_refuses_float_money(field):
    with pytest.raises(TypeError):
        make_quote(**{field: 1.5})


# A quote whose net is not amount minus fee is refused.
def test_quote_refuses_wrong_net():
    with pytest.raises(ValueError):
        make_quote(net=Decimal("998.00"))


# A quote cannot change after it is made.
def test_quote_is_frozen():
    with pytest.raises(FrozenInstanceError):
        make_quote().fee = Decimal("0")


# Any object with a minimum fee and rate_bps() counts as a FeeSchedule.
def test_fee_schedule_is_a_structural_interface():
    class Flat:
        minimum_fee = Decimal("1.00")

        def rate_bps(self, tier):
            return 50

    assert isinstance(Flat(), FeeSchedule)


# UnknownTier is a KeyError, so callers can catch either.
def test_unknown_tier_is_a_key_error():
    assert issubclass(UnknownTier, KeyError)
