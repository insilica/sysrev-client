from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Org")


@_attrs_define
class Org:
    """This is an object representing a Sysrev organization.

    Attributes:
        id (str):  Example: org_2.
        name (str):
        owner_user_id (str):  Example: user_139.
        is_enterprise (bool | Unset):
        enterprise_id (None | str | Unset):  Example: ent_2.
    """

    id: str
    name: str
    owner_user_id: str
    is_enterprise: bool | Unset = UNSET
    enterprise_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        owner_user_id = self.owner_user_id

        is_enterprise = self.is_enterprise

        enterprise_id: None | str | Unset
        if isinstance(self.enterprise_id, Unset):
            enterprise_id = UNSET
        else:
            enterprise_id = self.enterprise_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "owner_user_id": owner_user_id,
            }
        )
        if is_enterprise is not UNSET:
            field_dict["is_enterprise"] = is_enterprise
        if enterprise_id is not UNSET:
            field_dict["enterprise_id"] = enterprise_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        owner_user_id = d.pop("owner_user_id")

        is_enterprise = d.pop("is_enterprise", UNSET)

        def _parse_enterprise_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        enterprise_id = _parse_enterprise_id(d.pop("enterprise_id", UNSET))

        org = cls(
            id=id,
            name=name,
            owner_user_id=owner_user_id,
            is_enterprise=is_enterprise,
            enterprise_id=enterprise_id,
        )

        org.additional_properties = d
        return org

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
