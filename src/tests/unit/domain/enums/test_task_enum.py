from domain.enums.task_enum import TaskStatusEnum


def test_task_status_status_regex():
    assert TaskStatusEnum.status_regex() == "todo|doing|done"
