from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoLabelAnswer")


@_attrs_define
class AutoLabelAnswer:
    """
    Example:
        {'article_id': 'art_1', 'label_id': 'label_1', 'value': ['copper', 'nickel'], 'explanation': 'High levels of
            copper and nickel were found in the soil samples.', 'probability': 0.77}

    Attributes:
        article_id (str):  Example: art_1.
        label_id (str):  Example: label_1.
        explanation (str | Unset):
        probability (float | Unset):
    """

    article_id: str
    label_id: str
    explanation: str | Unset = UNSET
    probability: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        article_id = self.article_id

        label_id = self.label_id

        explanation = self.explanation

        probability = self.probability

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "article_id": article_id,
                "label_id": label_id,
            }
        )
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if probability is not UNSET:
            field_dict["probability"] = probability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        article_id = d.pop("article_id")

        label_id = d.pop("label_id")

        explanation = d.pop("explanation", UNSET)

        probability = d.pop("probability", UNSET)

        auto_label_answer = cls(
            article_id=article_id,
            label_id=label_id,
            explanation=explanation,
            probability=probability,
        )

        auto_label_answer.additional_properties = d
        return auto_label_answer

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
