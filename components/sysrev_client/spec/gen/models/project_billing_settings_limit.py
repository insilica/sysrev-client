from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_limit_strategy import BillingLimitStrategy

T = TypeVar("T", bound="ProjectBillingSettingsLimit")


@_attrs_define
class ProjectBillingSettingsLimit:
    """
    Attributes:
        strategy (BillingLimitStrategy): Limit by monthly or lifetime spend, or inherit owner restrictions.
        amount (int):
    """

    strategy: BillingLimitStrategy
    amount: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy = self.strategy.value

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strategy = BillingLimitStrategy(d.pop("strategy"))

        amount = d.pop("amount")

        project_billing_settings_limit = cls(
            strategy=strategy,
            amount=amount,
        )

        project_billing_settings_limit.additional_properties = d
        return project_billing_settings_limit

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
