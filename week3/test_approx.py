import pytest
from approx import find_cf
from pytest import approx

def test_find_cf():
    assert find_cf(7) == approx(43.974, abs=0.01)
    assert find_cf(7) == approx(43.982, abs=0.001)


pytest.main(["-v", "--tb=line", "-rN",__file__])
