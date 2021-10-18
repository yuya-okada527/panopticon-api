from enum import Enum


class TaskStatusEnum(Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"

    @classmethod
    def status_regex(self):
        return "|".join([status.value for status in TaskStatusEnum])
