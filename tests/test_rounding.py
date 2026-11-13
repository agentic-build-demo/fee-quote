"""Criterion 3: compute_fee rounds half up to cents and respects the minimum fee."""

from decimal import Decimal

import pytest

from feequote import compute_fee

ZERO = Decimal("0")


# A fee that is already whole cents comes back unchanged: 1000 at 25 bps is 2.50.
def test_exact_fee():
    assert compute_fee(Decimal("1000"), 25, ZERO) == Decimal("2.50")


# A fee that ends in exactly half a cent rounds up, not to the nearest even cent.
@pytest.mark.parametrize("amount, bps, expected", [
    (Decimal("1.00"), 50, Decimal("0.01")),   # 0.005 -> 0.01
    (Decimal("10"), 25, Decimal("0.03")),     # 0.025 -> 0.03 (banker's rounding would give 0.02)
    (Decimal("10"), 15, Decimal("0.02")),     # 0.015 -> 0.02
])
def test_half_cent_rounds_up(amount, bps, expected):
    assert compute_fee(amount, bps, ZERO) == expected


# Below half a cent rounds down.
def test_below_half_cent_rounds_down():
    assert compute_fee(Decimal("10"), 4, ZERO) == Decimal("0.00")   # 0.004 -> 0.00


# A fee under the minimum is raised to the minimum: 100 at 25 bps is 0.25, minimum 1.00.
def test_minimum_fee_applies():
    assert compute_fee(Decimal("100"), 25, Decimal("1.00")) == Decimal("1.00")


# A fee over the minimum is not changed by it.
def test_minimum_fee_does_not_raise_a_larger_fee():
    assert compute_fee(Decimal("10000"), 25, Decimal("1.00")) == Decimal("25.00")


# The result is a Decimal with exactly two decimal places.
def test_result_is_decimal_cents():
    fee = compute_fee(Decimal("1234.5678"), 33, ZERO)
    assert isinstance(fee, Decimal)
    assert fee.as_tuple().exponent == -2
