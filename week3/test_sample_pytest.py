from sample_pytest import subtract
import pytest

def test_subtract():
    assert subtract(0,0) == 0
    assert subtract(-1,0) == -1
    assert subtract(-1,-1) == 0, "not 0"



pytest.main(["-v", "--tb=line", "-rN",__file__])