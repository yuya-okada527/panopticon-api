import pytest
from entrypoints.helper.base_helper import calc_available_page


@pytest.mark.parametrize("args", [[1, 2, 2], [2, 3, 2], [0, 10, 0]])
def test_calc_available_page(args):
    num, hit_num, expected = args
    assert calc_available_page(num, hit_num) == expected
