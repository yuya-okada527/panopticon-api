import pytest
from entrypoints.helper.base_helper import calc_available_page, calc_offset


@pytest.mark.parametrize("args", [[1, 2, 2], [2, 3, 2], [0, 10, 0]])
def test_calc_available_page(args):
    num, hit_num, expected = args
    assert calc_available_page(num, hit_num) == expected


@pytest.mark.parametrize("args", [[1, 2, 0], [2, 3, 3], [3, 3, 6]])
def test_calc_offset(args):
    page, num, expected = args
    assert calc_offset(page, num) == expected
