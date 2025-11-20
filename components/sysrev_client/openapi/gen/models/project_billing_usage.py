from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_limit_strategy import BillingLimitStrategy
from ..models.billing_usage_period import BillingUsagePeriod
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectBillingUsage")


@_attrs_define
class ProjectBillingUsage:
    """This is an object representing an account's usage for a given billing period.

    Attributes:
        total (int):
        usage (int):
        available (int):
        lifetime_usage (int | Unset):
        usage_period (BillingUsagePeriod | Unset): The period by which the usage amount is tracked.
        monthly_usage (int | Unset):
        limit_strategy (BillingLimitStrategy | Unset): Limit by monthly or lifetime spend, or inherit owner
            restrictions.
        unused_limit (int | Unset):
        pending_charges (int | Unset):
    """

    total: int
    usage: int
    available: int
    lifetime_usage: int | Unset = UNSET
    usage_period: BillingUsagePeriod | Unset = UNSET
    monthly_usage: int | Unset = UNSET
    limit_strategy: BillingLimitStrategy | Unset = UNSET
    unused_limit: int | Unset = UNSET
    pending_charges: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        usage = self.usage

        available = self.available

        lifetime_usage = self.lifetime_usage

        usage_period: str | Unset = UNSET
        if not isinstance(self.usage_period, Unset):
            usage_period = self.usage_period.value

        monthly_usage = self.monthly_usage

        limit_strategy: str | Unset = UNSET
        if not isinstance(self.limit_strategy, Unset):
            limit_strategy = self.limit_strategy.value

        unused_limit = self.unused_limit

        pending_charges = self.pending_charges

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "usage": usage,
                "available": available,
            }
        )
        if lifetime_usage is not UNSET:
            field_dict["lifetime_usage"] = lifetime_usage
        if usage_period is not UNSET:
            field_dict["usage_period"] = usage_period
        if monthly_usage is not UNSET:
            field_dict["monthly_usage"] = monthly_usage
        if limit_strategy is not UNSET:
            field_dict["limit_strategy"] = limit_strategy
        if unused_limit is not UNSET:
            field_dict["unused_limit"] = unused_limit
        if pending_charges is not UNSET:
            field_dict["pending_charges"] = pending_charges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        usage = d.pop("usage")

        available = d.pop("available")

        lifetime_usage = d.pop("lifetime_usage", UNSET)

        _usage_period = d.pop("usage_period", UNSET)
        usage_period: BillingUsagePeriod | Unset
        if isinstance(_usage_period, Unset):
            usage_period = UNSET
        else:
            usage_period = BillingUsagePeriod(_usage_period)

        monthly_usage = d.pop("monthly_usage", UNSET)

        _limit_strategy = d.pop("limit_strategy", UNSET)
        limit_strategy: BillingLimitStrategy | Unset
        if isinstance(_limit_strategy, Unset):
            limit_strategy = UNSET
        else:
            limit_strategy = BillingLimitStrategy(_limit_strategy)

        unused_limit = d.pop("unused_limit", UNSET)

        pending_charges = d.pop("pending_charges", UNSET)

        project_billing_usage = cls(
            total=total,
            usage=usage,
            available=available,
            lifetime_usage=lifetime_usage,
            usage_period=usage_period,
            monthly_usage=monthly_usage,
            limit_strategy=limit_strategy,
            unused_limit=unused_limit,
            pending_charges=pending_charges,
        )

        project_billing_usage.additional_properties = d
        return project_billing_usage

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
