from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.article_full_text_content_blob import ArticleFullTextContentBlob
    from ..models.article_full_text_content_json import ArticleFullTextContentJson


T = TypeVar("T", bound="ArticleFullText")


@_attrs_define
class ArticleFullText:
    """This is an object representing a source of articles.

    Attributes:
        file_name (str):
        content (ArticleFullTextContentBlob | ArticleFullTextContentJson): This is an object representing a source of
            articles.
    """

    file_name: str
    content: ArticleFullTextContentBlob | ArticleFullTextContentJson
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.article_full_text_content_json import ArticleFullTextContentJson

        file_name = self.file_name

        content: dict[str, Any]
        if isinstance(self.content, ArticleFullTextContentJson):
            content = self.content.to_dict()
        else:
            content = self.content.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_name": file_name,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_full_text_content_blob import ArticleFullTextContentBlob
        from ..models.article_full_text_content_json import ArticleFullTextContentJson

        d = dict(src_dict)
        file_name = d.pop("file_name")

        def _parse_content(data: object) -> ArticleFullTextContentBlob | ArticleFullTextContentJson:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_article_full_text_content_type_0 = ArticleFullTextContentJson.from_dict(data)

                return componentsschemas_article_full_text_content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_article_full_text_content_type_1 = ArticleFullTextContentBlob.from_dict(data)

            return componentsschemas_article_full_text_content_type_1

        content = _parse_content(d.pop("content"))

        article_full_text = cls(
            file_name=file_name,
            content=content,
        )

        article_full_text.additional_properties = d
        return article_full_text

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
