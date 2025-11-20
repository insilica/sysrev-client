from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_billing_settings_limit import ProjectBillingSettingsLimit


T = TypeVar("T", bound="ProjectBillingSettings")


@_attrs_define
class ProjectBillingSettings:
    """This is an object representing an project's billing settings.

    Attributes:
        limit (ProjectBillingSettingsLimit):
    """

    limit: ProjectBillingSettingsLimit
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_billing_settings_limit import ProjectBillingSettingsLimit

        d = dict(src_dict)
        limit = ProjectBillingSettingsLimit.from_dict(d.pop("limit"))

        project_billing_settings = cls(
            limit=limit,
        )

        project_billing_settings.additional_properties = d
        return project_billing_settings

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
