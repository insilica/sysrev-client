from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_label_answer_updated_request_event_type import AutoLabelAnswerUpdatedRequestEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_label_answer import AutoLabelAnswer


T = TypeVar("T", bound="AutoLabelAnswerUpdatedRequest")


@_attrs_define
class AutoLabelAnswerUpdatedRequest:
    """
    Attributes:
        event_type (AutoLabelAnswerUpdatedRequestEventType):
        auto_label_answers (list[AutoLabelAnswer] | Unset):
    """

    event_type: AutoLabelAnswerUpdatedRequestEventType
    auto_label_answers: list[AutoLabelAnswer] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        auto_label_answers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auto_label_answers, Unset):
            auto_label_answers = []
            for auto_label_answers_item_data in self.auto_label_answers:
                auto_label_answers_item = auto_label_answers_item_data.to_dict()
                auto_label_answers.append(auto_label_answers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
            }
        )
        if auto_label_answers is not UNSET:
            field_dict["auto_label_answers"] = auto_label_answers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_label_answer import AutoLabelAnswer

        d = dict(src_dict)
        event_type = AutoLabelAnswerUpdatedRequestEventType(d.pop("event_type"))

        _auto_label_answers = d.pop("auto_label_answers", UNSET)
        auto_label_answers: list[AutoLabelAnswer] | Unset = UNSET
        if _auto_label_answers is not UNSET:
            auto_label_answers = []
            for auto_label_answers_item_data in _auto_label_answers:
                auto_label_answers_item = AutoLabelAnswer.from_dict(auto_label_answers_item_data)

                auto_label_answers.append(auto_label_answers_item)

        auto_label_answer_updated_request = cls(
            event_type=event_type,
            auto_label_answers=auto_label_answers,
        )

        auto_label_answer_updated_request.additional_properties = d
        return auto_label_answer_updated_request

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
