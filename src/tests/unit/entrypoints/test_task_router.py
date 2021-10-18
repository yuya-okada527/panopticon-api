import json

import pytest
from domain.enums.task_enum import TaskStatusEnum
from fastapi.testclient import TestClient
from tests.utils import TASK_API_PATH, make_url


@pytest.mark.parametrize("params", [[], ["page=0"], ["num=0"], ["num=100"]])
def test_search_tasks_200(test_client: TestClient, params):
    assert (
        test_client.get(make_url(TASK_API_PATH, params)).status_code == 200
    ), f"params={params} must be valid params"


@pytest.mark.parametrize("params", [["page=str"], ["page=-1"], ["num=-1"], ["num=101"]])
def test_search_tasks_422(test_client: TestClient, params):
    assert (
        test_client.get(make_url(TASK_API_PATH, params)).status_code == 422
    ), f"params={params} must be invalid params"


@pytest.mark.parametrize(
    "data",
    [{"name": "test", "status": status.value} for status in TaskStatusEnum]
    + [{"name": "a", "status": "todo"}, {"name": "a" * 64, "status": "todo"}],
)
def test_create_task_200(test_client: TestClient, data):
    assert (
        test_client.post(TASK_API_PATH, json.dumps(data)).status_code == 200
    ), f"data={data} must be valid data"


@pytest.mark.parametrize(
    "data",
    [
        {},
        {"name": ""},
        {"status": "todo"},
        {"name": "a" * 65},
        {"name": "test", "status": "test"},
    ],
)
def test_create_task_422(test_client: TestClient, data):
    assert (
        test_client.post(TASK_API_PATH, json.dumps(data)).status_code == 422
    ), f"data={data} must be invalid data"
