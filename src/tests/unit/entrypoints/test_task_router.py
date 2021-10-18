import pytest
from fastapi.testclient import TestClient
from tests.utils import TASK_API_PATH, make_url


@pytest.mark.parametrize("params", [[]])
def test_search_tasks_200(test_client: TestClient, params):
    assert (
        test_client.get(make_url(TASK_API_PATH, params)).status_code == 200
    ), f"params={params} must be valid params"
