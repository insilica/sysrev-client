from enum import Enum


class WebhookEventTypesItems(str, Enum):
    AUTO_LABEL_ANSWER_UPDATED = "auto_label_answer.updated"
    VALUE_0 = "*"

    def __str__(self) -> str:
        return str(self.value)
