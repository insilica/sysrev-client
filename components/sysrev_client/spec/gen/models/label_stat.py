from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelStat")


@_attrs_define
class LabelStat:
    """
    Attributes:
        short_label (str | Unset):
        label_id (UUID | Unset):
        value_type (str | Unset):
        project_ordering (int | Unset):
        count (int | Unset):
    """

    short_label: str | Unset = UNSET
    label_id: UUID | Unset = UNSET
    value_type: str | Unset = UNSET
    project_ordering: int | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        short_label = self.short_label

        label_id: str | Unset = UNSET
        if not isinstance(self.label_id, Unset):
            label_id = str(self.label_id)

        value_type = self.value_type

        project_ordering = self.project_ordering

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if short_label is not UNSET:
            field_dict["short_label"] = short_label
        if label_id is not UNSET:
            field_dict["label_id"] = label_id
        if value_type is not UNSET:
            field_dict["value_type"] = value_type
        if project_ordering is not UNSET:
            field_dict["project_ordering"] = project_ordering
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        short_label = d.pop("short_label", UNSET)

        _label_id = d.pop("label_id", UNSET)
        label_id: UUID | Unset
        if isinstance(_label_id, Unset):
            label_id = UNSET
        else:
            label_id = UUID(_label_id)

        value_type = d.pop("value_type", UNSET)

        project_ordering = d.pop("project_ordering", UNSET)

        count = d.pop("count", UNSET)

        label_stat = cls(
            short_label=short_label,
            label_id=label_id,
            value_type=value_type,
            project_ordering=project_ordering,
            count=count,
        )

        label_stat.additional_properties = d
        return label_stat

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
