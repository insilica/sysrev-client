from enum import Enum


class ProjectExportType(str, Enum):
    PARQUET = "parquet"

    def __str__(self) -> str:
        return str(self.value)
