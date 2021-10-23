import pytest
from starlette.testclient import TestClient

# 定数定義
STATUS_API_PATH = "/v1/statuses"


def test_search_statues_200(test_client: TestClient):
    assert test_client.get(STATUS_API_PATH).status_code == 200
