from enum import Enum


class ProjectExportStatus(str, Enum):
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
