from enum import Enum


class AutoLabelAnswerUpdatedRequestEventType(str, Enum):
    AUTO_LABEL_ANSWER_UPDATED = "auto_label_answer.updated"

    def __str__(self) -> str:
        return str(self.value)
