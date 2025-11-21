from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateEnterpriseInput")


@_attrs_define
class CreateEnterpriseInput:
    """
    Attributes:
        root_org_id (str): The root organization of the enterprise. Admins of this org will have access to other orgs
            within the enterprise. Example: org_2.
        user_id (str): ID of a user whose Stripe customer id will be used for the enterprise.
                     The user can be created just for the enterprise and need not be the account of a human user. Example:
            user_139.
    """

    root_org_id: str
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        root_org_id = self.root_org_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "root_org_id": root_org_id,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        root_org_id = d.pop("root_org_id")

        user_id = d.pop("user_id")

        create_enterprise_input = cls(
            root_org_id=root_org_id,
            user_id=user_id,
        )

        create_enterprise_input.additional_properties = d
        return create_enterprise_input

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
