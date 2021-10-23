import pytest
from domain.models.task_model import Task


@pytest.mark.parametrize("args", [["status", Task.status]])
def test_task_order_key(args):
    key, expected = args
    assert Task.order_key(key) == expected
