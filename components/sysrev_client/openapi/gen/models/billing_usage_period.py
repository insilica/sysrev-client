from enum import Enum


class BillingUsagePeriod(str, Enum):
    LIFETIME = "lifetime"
    MONTHLY = "monthly"

    def __str__(self) -> str:
        return str(self.value)
