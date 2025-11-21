from enum import Enum


class BillingLimitStrategy(str, Enum):
    LIFETIME = "lifetime"
    MONTHLY = "monthly"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
