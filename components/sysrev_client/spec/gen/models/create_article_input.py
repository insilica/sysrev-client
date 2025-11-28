from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_full_text import ArticleFullText
    from ..models.create_article_input_citation import CreateArticleInputCitation


T = TypeVar("T", bound="CreateArticleInput")


@_attrs_define
class CreateArticleInput:
    """
    Example:
        {'source_id': 'src_8293', 'citation': {'title': 'Hello world', 'type': 'article-journal'}, 'full_texts':
            [{'file_name': 'president_16.json', 'content': {'json': {'first_name': 'Abraham', 'last_name': 'Lincoln'}}},
            {'file_name': 'hello_world.pdf', 'content': {'file_data': {'mime_type': 'application/pdf', 'data': '<B64
            string>'}}}]}

    Attributes:
        source_id (str):  Example: src_1.
        citation (CreateArticleInputCitation | Unset):
        full_texts (list[ArticleFullText] | Unset):
    """

    source_id: str
    citation: CreateArticleInputCitation | Unset = UNSET
    full_texts: list[ArticleFullText] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_id = self.source_id

        citation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.citation, Unset):
            citation = self.citation.to_dict()

        full_texts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.full_texts, Unset):
            full_texts = []
            for full_texts_item_data in self.full_texts:
                full_texts_item = full_texts_item_data.to_dict()
                full_texts.append(full_texts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_id": source_id,
            }
        )
        if citation is not UNSET:
            field_dict["citation"] = citation
        if full_texts is not UNSET:
            field_dict["full_texts"] = full_texts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_full_text import ArticleFullText
        from ..models.create_article_input_citation import CreateArticleInputCitation

        d = dict(src_dict)
        source_id = d.pop("source_id")

        _citation = d.pop("citation", UNSET)
        citation: CreateArticleInputCitation | Unset
        if isinstance(_citation, Unset):
            citation = UNSET
        else:
            citation = CreateArticleInputCitation.from_dict(_citation)

        _full_texts = d.pop("full_texts", UNSET)
        full_texts: list[ArticleFullText] | Unset = UNSET
        if _full_texts is not UNSET:
            full_texts = []
            for full_texts_item_data in _full_texts:
                full_texts_item = ArticleFullText.from_dict(full_texts_item_data)

                full_texts.append(full_texts_item)

        create_article_input = cls(
            source_id=source_id,
            citation=citation,
            full_texts=full_texts,
        )

        create_article_input.additional_properties = d
        return create_article_input

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
