import json

import pytest
from domain.enums.task_enum import TaskStatusEnum
from domain.models.task_model import Task
from fastapi.testclient import TestClient
from tests.utils import make_url

# 定数定義
TASK_API_PATH = "/v1/tasks"
MODULE_PATH = "entrypoints.task_router"


@pytest.mark.parametrize("params", [[], ["page=1"], ["num=0"], ["num=100"]])
def test_search_tasks_200(test_client: TestClient, mocker, params):
    mocker.patch(f"{MODULE_PATH}.search_tasks_service", return_value=[[], 0])
    assert (
        test_client.get(make_url(TASK_API_PATH, params)).status_code == 200
    ), f"params={params} must be valid"


@pytest.mark.parametrize(
    "params", [["page=str"], ["page=0"], ["page=-1"], ["num=-1"], ["num=101"]]
)
def test_search_tasks_422(test_client: TestClient, params):
    assert (
        test_client.get(make_url(TASK_API_PATH, params)).status_code == 422
    ), f"params={params} must be invalid"


@pytest.mark.parametrize(
    "data",
    [{"name": "test", "status": status.value} for status in TaskStatusEnum]
    + [
        {"name": "a", "status": "todo"},
        {"name": "a" * 64, "status": "todo"},
        {"name": "a b", "status": "todo"},
    ],
)
def test_create_task_200(test_client: TestClient, mocker, data):
    mocker.patch(f"{MODULE_PATH}.create_task_service", return_value=0)
    assert (
        test_client.post(TASK_API_PATH, json.dumps(data)).status_code == 200
    ), f"data={data} must be valid"


@pytest.mark.parametrize(
    "data",
    [
        {},
        {"name": ""},
        {"name": " \n\t\r\n"},
        {"status": "todo"},
        {"name": "a" * 65},
        {"name": "test", "status": "test"},
    ],
)
def test_create_task_422(test_client: TestClient, data):
    assert (
        test_client.post(TASK_API_PATH, json.dumps(data)).status_code == 422
    ), f"data={data} must be invalid"


@pytest.mark.parametrize(
    "data",
    [{}, {"name": "test"}, {"status": "todo"}, {"name": "test", "status": "doing"}],
)
def test_update_task_200_data(test_client: TestClient, mocker, data):
    mocker.patch(f"{MODULE_PATH}.update_task_service", return_value=0)
    assert (
        test_client.put(f"{TASK_API_PATH}/1", json.dumps(data)).status_code == 200
    ), f"data={data} must be valid"


@pytest.mark.parametrize("path", [0])
def test_update_task_200_path(test_client: TestClient, mocker, path):
    mocker.patch(f"{MODULE_PATH}.update_task_service", return_value=0)
    assert (
        test_client.put(f"{TASK_API_PATH}/{path}", json.dumps({})).status_code == 200
    ), f"path={path} must be valid"


def test_update_task_404(test_client: TestClient, mocker):
    mocker.patch(f"{MODULE_PATH}.update_task_service", return_value=None)
    assert test_client.put(f"{TASK_API_PATH}/1", json.dumps({})).status_code == 404


@pytest.mark.parametrize("path", [-1, "test"])
def test_update_tasl_422_path(test_client: TestClient, path):
    assert (
        test_client.put(f"{TASK_API_PATH}/{path}", json.dumps({})).status_code == 422
    ), f"path={path} must be invalid"


@pytest.mark.parametrize("data", [{"name": ""}, {"status": "test"}, {"name": " "}])
def test_update_task_422_data(test_client: TestClient, data):
    assert (
        test_client.put(f"{TASK_API_PATH}/1", json.dumps(data)).status_code == 422
    ), f"data={data} must be invalid"


@pytest.mark.parametrize("path", [0])
def test_delete_task_200(test_client: TestClient, mocker, path):
    mocker.patch(f"{MODULE_PATH}.delete_task_service", return_value=0)
    assert (
        test_client.delete(f"{TASK_API_PATH}/{path}").status_code == 200
    ), f"path={path} must be valid"


def test_delete_task_404(test_client: TestClient, mocker):
    mocker.patch(f"{MODULE_PATH}.delete_task_service", return_value=None)
    assert test_client.delete(f"{TASK_API_PATH}/1").status_code == 404


@pytest.mark.parametrize("path", [-1, "test"])
def test_delete_task_422(test_client: TestClient, path):
    assert (
        test_client.delete(f"{TASK_API_PATH}/{path}").status_code == 422
    ), f"path={path} must be invalid"


@pytest.mark.parametrize("path", [1])
def test_read_task_200(test_client: TestClient, mocker, path):
    mocker.patch(
        f"{MODULE_PATH}.read_task_service",
        return_value=Task(id=1, name="name", status="todo"),
    )
    assert (
        test_client.get(f"{TASK_API_PATH}/{path}").status_code == 200
    ), f"path={path} must be invalid"


def test_read_task_404(test_client: TestClient, mocker):
    mocker.patch(f"{MODULE_PATH}.read_task_service", return_value=None)
    assert test_client.get(f"{TASK_API_PATH}/1").status_code == 404


@pytest.mark.parametrize("path", [-1, "str"])
def test_read_task_422(test_client: TestClient, path):
    assert (
        test_client.get(f"{TASK_API_PATH}/{path}").status_code == 422
    ), f"path={path} must be invalid"
