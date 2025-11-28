from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloneProjectInput")


@_attrs_define
class CloneProjectInput:
    """
    Attributes:
        owner_id (str): The ID of the user or organization that will be the owner of the new cloned project. Example:
            user_1.
        copy_articles (bool | Unset): Whether to copy articles to the new project. Default: True.
        copy_label_answers (bool | Unset): Whether to copy label answers to the new project. Default: True.
        copy_labels (bool | Unset): Whether to copy labels to the new project. Default: True.
    """

    owner_id: str
    copy_articles: bool | Unset = True
    copy_label_answers: bool | Unset = True
    copy_labels: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        copy_articles = self.copy_articles

        copy_label_answers = self.copy_label_answers

        copy_labels = self.copy_labels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner_id": owner_id,
            }
        )
        if copy_articles is not UNSET:
            field_dict["copy_articles"] = copy_articles
        if copy_label_answers is not UNSET:
            field_dict["copy_label_answers"] = copy_label_answers
        if copy_labels is not UNSET:
            field_dict["copy_labels"] = copy_labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("owner_id")

        copy_articles = d.pop("copy_articles", UNSET)

        copy_label_answers = d.pop("copy_label_answers", UNSET)

        copy_labels = d.pop("copy_labels", UNSET)

        clone_project_input = cls(
            owner_id=owner_id,
            copy_articles=copy_articles,
            copy_label_answers=copy_label_answers,
            copy_labels=copy_labels,
        )

        clone_project_input.additional_properties = d
        return clone_project_input

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
