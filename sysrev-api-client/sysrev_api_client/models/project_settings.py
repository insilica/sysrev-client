from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectSettings")


@_attrs_define
class ProjectSettings:
    """
    Attributes:
        auto_save_labels (bool | Unset): Automatically save review labels
        blind_reviewers (bool | Unset): Label blinding
        enabled (bool | Unset): Project enabled
        freeze_model (bool | Unset): Freeze model
        public_access (bool | Unset): Project visibility
        second_review_prob (float | str | Unset):
        unlimited_reviews (bool | Unset): Allow unlimited reviews
    """

    auto_save_labels: bool | Unset = UNSET
    blind_reviewers: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    freeze_model: bool | Unset = UNSET
    public_access: bool | Unset = UNSET
    second_review_prob: float | str | Unset = UNSET
    unlimited_reviews: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_save_labels = self.auto_save_labels

        blind_reviewers = self.blind_reviewers

        enabled = self.enabled

        freeze_model = self.freeze_model

        public_access = self.public_access

        second_review_prob: float | str | Unset
        if isinstance(self.second_review_prob, Unset):
            second_review_prob = UNSET
        else:
            second_review_prob = self.second_review_prob

        unlimited_reviews = self.unlimited_reviews

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_save_labels is not UNSET:
            field_dict["auto_save_labels"] = auto_save_labels
        if blind_reviewers is not UNSET:
            field_dict["blind_reviewers"] = blind_reviewers
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if freeze_model is not UNSET:
            field_dict["freeze_model"] = freeze_model
        if public_access is not UNSET:
            field_dict["public_access"] = public_access
        if second_review_prob is not UNSET:
            field_dict["second_review_prob"] = second_review_prob
        if unlimited_reviews is not UNSET:
            field_dict["unlimited_reviews"] = unlimited_reviews

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_save_labels = d.pop("auto_save_labels", UNSET)

        blind_reviewers = d.pop("blind_reviewers", UNSET)

        enabled = d.pop("enabled", UNSET)

        freeze_model = d.pop("freeze_model", UNSET)

        public_access = d.pop("public_access", UNSET)

        def _parse_second_review_prob(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        second_review_prob = _parse_second_review_prob(d.pop("second_review_prob", UNSET))

        unlimited_reviews = d.pop("unlimited_reviews", UNSET)

        project_settings = cls(
            auto_save_labels=auto_save_labels,
            blind_reviewers=blind_reviewers,
            enabled=enabled,
            freeze_model=freeze_model,
            public_access=public_access,
            second_review_prob=second_review_prob,
            unlimited_reviews=unlimited_reviews,
        )

        project_settings.additional_properties = d
        return project_settings

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
