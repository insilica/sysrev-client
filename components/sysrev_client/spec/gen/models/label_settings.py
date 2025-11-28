from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelSettings")


@_attrs_define
class LabelSettings:
    """
    Attributes:
        hidden (bool | Unset):
        enabled (bool | Unset):
        consensus (bool | Unset):
        overall_include (bool | Unset):
        auto_label_enabled (bool | Unset):
        auto_label_full_text (bool | Unset):
        auto_label_reasoning (bool | Unset):
        auto_label_model (str | Unset):
    """

    hidden: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    consensus: bool | Unset = UNSET
    overall_include: bool | Unset = UNSET
    auto_label_enabled: bool | Unset = UNSET
    auto_label_full_text: bool | Unset = UNSET
    auto_label_reasoning: bool | Unset = UNSET
    auto_label_model: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hidden = self.hidden

        enabled = self.enabled

        consensus = self.consensus

        overall_include = self.overall_include

        auto_label_enabled = self.auto_label_enabled

        auto_label_full_text = self.auto_label_full_text

        auto_label_reasoning = self.auto_label_reasoning

        auto_label_model = self.auto_label_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if consensus is not UNSET:
            field_dict["consensus"] = consensus
        if overall_include is not UNSET:
            field_dict["overall_include"] = overall_include
        if auto_label_enabled is not UNSET:
            field_dict["auto_label_enabled"] = auto_label_enabled
        if auto_label_full_text is not UNSET:
            field_dict["auto_label_full_text"] = auto_label_full_text
        if auto_label_reasoning is not UNSET:
            field_dict["auto_label_reasoning"] = auto_label_reasoning
        if auto_label_model is not UNSET:
            field_dict["auto_label_model"] = auto_label_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hidden = d.pop("hidden", UNSET)

        enabled = d.pop("enabled", UNSET)

        consensus = d.pop("consensus", UNSET)

        overall_include = d.pop("overall_include", UNSET)

        auto_label_enabled = d.pop("auto_label_enabled", UNSET)

        auto_label_full_text = d.pop("auto_label_full_text", UNSET)

        auto_label_reasoning = d.pop("auto_label_reasoning", UNSET)

        auto_label_model = d.pop("auto_label_model", UNSET)

        label_settings = cls(
            hidden=hidden,
            enabled=enabled,
            consensus=consensus,
            overall_include=overall_include,
            auto_label_enabled=auto_label_enabled,
            auto_label_full_text=auto_label_full_text,
            auto_label_reasoning=auto_label_reasoning,
            auto_label_model=auto_label_model,
        )

        label_settings.additional_properties = d
        return label_settings

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
