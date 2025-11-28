from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.auto_article_label_reasoning_type_0 import AutoArticleLabelReasoningType0


T = TypeVar("T", bound="AutoArticleLabel")


@_attrs_define
class AutoArticleLabel:
    """
    Example:
        {'label_id': 'label_1', 'reasoning': None, 'probability': 0.77, 'is_failure': False, 'article_id': 'art_1',
            'value': ['copper', 'nickel'], 'auto_label_run_id': 'alr_1', 'created_at': 1763611713703, 'explanation': 'High
            levels of copper and nickel were found in the soil samples.', 'is_pending': False}

    Attributes:
        label_id (str):
        reasoning (AutoArticleLabelReasoningType0 | None):
        probability (float | None):
        is_failure (bool):
        article_id (str):
        auto_label_run_id (str):
        created_at (int):
        explanation (str):
        is_pending (bool):
    """

    label_id: str
    reasoning: AutoArticleLabelReasoningType0 | None
    probability: float | None
    is_failure: bool
    article_id: str
    auto_label_run_id: str
    created_at: int
    explanation: str
    is_pending: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.auto_article_label_reasoning_type_0 import AutoArticleLabelReasoningType0

        label_id = self.label_id

        reasoning: dict[str, Any] | None
        if isinstance(self.reasoning, AutoArticleLabelReasoningType0):
            reasoning = self.reasoning.to_dict()
        else:
            reasoning = self.reasoning

        probability: float | None
        probability = self.probability

        is_failure = self.is_failure

        article_id = self.article_id

        auto_label_run_id = self.auto_label_run_id

        created_at = self.created_at

        explanation = self.explanation

        is_pending = self.is_pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label_id": label_id,
                "reasoning": reasoning,
                "probability": probability,
                "is_failure": is_failure,
                "article_id": article_id,
                "auto_label_run_id": auto_label_run_id,
                "created_at": created_at,
                "explanation": explanation,
                "is_pending": is_pending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_article_label_reasoning_type_0 import AutoArticleLabelReasoningType0

        d = dict(src_dict)
        label_id = d.pop("label_id")

        def _parse_reasoning(data: object) -> AutoArticleLabelReasoningType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reasoning_type_0 = AutoArticleLabelReasoningType0.from_dict(data)

                return reasoning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutoArticleLabelReasoningType0 | None, data)

        reasoning = _parse_reasoning(d.pop("reasoning"))

        def _parse_probability(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        probability = _parse_probability(d.pop("probability"))

        is_failure = d.pop("is_failure")

        article_id = d.pop("article_id")

        auto_label_run_id = d.pop("auto_label_run_id")

        created_at = d.pop("created_at")

        explanation = d.pop("explanation")

        is_pending = d.pop("is_pending")

        auto_article_label = cls(
            label_id=label_id,
            reasoning=reasoning,
            probability=probability,
            is_failure=is_failure,
            article_id=article_id,
            auto_label_run_id=auto_label_run_id,
            created_at=created_at,
            explanation=explanation,
            is_pending=is_pending,
        )

        auto_article_label.additional_properties = d
        return auto_article_label

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
