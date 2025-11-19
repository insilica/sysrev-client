from enum import Enum


class ArticleSuppressionType(str, Enum):
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
