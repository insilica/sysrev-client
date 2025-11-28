from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProjectInput")


@_attrs_define
class CreateProjectInput:
    """
    Attributes:
        is_public (bool): Whether the project is public. If true, the project will be publicly visible. If false, the
            project will be visible only to its members.
        name (str): The name of the project. Must be 40 characters or less. May only contain letters, numbers, and
            hyphens. It may not start or end with a hyphen.
        org_id (str | Unset): Optional organization to assign the new project to.
    """

    is_public: bool
    name: str
    org_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_public = self.is_public

        name = self.name

        org_id = self.org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_public": is_public,
                "name": name,
            }
        )
        if org_id is not UNSET:
            field_dict["org_id"] = org_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_public = d.pop("is_public")

        name = d.pop("name")

        org_id = d.pop("org_id", UNSET)

        create_project_input = cls(
            is_public=is_public,
            name=name,
            org_id=org_id,
        )

        create_project_input.additional_properties = d
        return create_project_input

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
