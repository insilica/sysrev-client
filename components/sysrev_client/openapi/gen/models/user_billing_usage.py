from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_limit_strategy import BillingLimitStrategy
from ..models.billing_usage_period import BillingUsagePeriod

T = TypeVar("T", bound="UserBillingUsage")


@_attrs_define
class UserBillingUsage:
    """This is an object representing an account's usage for a given billing period.

    Attributes:
        total (int):
        usage (int):
        credit (int):
        usage_period (BillingUsagePeriod): The period by which the usage amount is tracked.
        monthly (int):
        limit_strategy (BillingLimitStrategy): Limit by monthly or lifetime spend, or inherit owner restrictions.
        unused_limit (int):
        pending_charges (int):
        available (int):
    """

    total: int
    usage: int
    credit: int
    usage_period: BillingUsagePeriod
    monthly: int
    limit_strategy: BillingLimitStrategy
    unused_limit: int
    pending_charges: int
    available: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        usage = self.usage

        credit = self.credit

        usage_period = self.usage_period.value

        monthly = self.monthly

        limit_strategy = self.limit_strategy.value

        unused_limit = self.unused_limit

        pending_charges = self.pending_charges

        available = self.available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "usage": usage,
                "credit": credit,
                "usage_period": usage_period,
                "monthly": monthly,
                "limit_strategy": limit_strategy,
                "unused_limit": unused_limit,
                "pending_charges": pending_charges,
                "available": available,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        usage = d.pop("usage")

        credit = d.pop("credit")

        usage_period = BillingUsagePeriod(d.pop("usage_period"))

        monthly = d.pop("monthly")

        limit_strategy = BillingLimitStrategy(d.pop("limit_strategy"))

        unused_limit = d.pop("unused_limit")

        pending_charges = d.pop("pending_charges")

        available = d.pop("available")

        user_billing_usage = cls(
            total=total,
            usage=usage,
            credit=credit,
            usage_period=usage_period,
            monthly=monthly,
            limit_strategy=limit_strategy,
            unused_limit=unused_limit,
            pending_charges=pending_charges,
            available=available,
        )

        user_billing_usage.additional_properties = d
        return user_billing_usage

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
