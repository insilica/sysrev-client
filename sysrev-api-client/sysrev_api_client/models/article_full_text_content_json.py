from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.article_full_text_content_json_json_type_1 import ArticleFullTextContentJsonJsonType1


T = TypeVar("T", bound="ArticleFullTextContentJson")


@_attrs_define
class ArticleFullTextContentJson:
    """
    Attributes:
        json (ArticleFullTextContentJsonJsonType1 | str):
    """

    json: ArticleFullTextContentJsonJsonType1 | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.article_full_text_content_json_json_type_1 import ArticleFullTextContentJsonJsonType1

        json: dict[str, Any] | str
        if isinstance(self.json, ArticleFullTextContentJsonJsonType1):
            json = self.json.to_dict()
        else:
            json = self.json

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "json": json,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_full_text_content_json_json_type_1 import ArticleFullTextContentJsonJsonType1

        d = dict(src_dict)

        def _parse_json(data: object) -> ArticleFullTextContentJsonJsonType1 | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                json_type_1 = ArticleFullTextContentJsonJsonType1.from_dict(data)

                return json_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ArticleFullTextContentJsonJsonType1 | str, data)

        json = _parse_json(d.pop("json"))

        article_full_text_content_json = cls(
            json=json,
        )

        article_full_text_content_json.additional_properties = d
        return article_full_text_content_json

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
