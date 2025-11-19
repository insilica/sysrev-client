from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Enterprise")


@_attrs_define
class Enterprise:
    """This is an object representing an enterprise.

    Attributes:
        id (str):  Example: ent_2.
        org_ids (list[str]):
        created_at (int | Unset):
        name (str | Unset):
    """

    id: str
    org_ids: list[str]
    created_at: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        org_ids = self.org_ids

        created_at = self.created_at

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_ids": org_ids,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        org_ids = cast(list[str], d.pop("org_ids"))

        created_at = d.pop("created_at", UNSET)

        name = d.pop("name", UNSET)

        enterprise = cls(
            id=id,
            org_ids=org_ids,
            created_at=created_at,
            name=name,
        )

        enterprise.additional_properties = d
        return enterprise

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
