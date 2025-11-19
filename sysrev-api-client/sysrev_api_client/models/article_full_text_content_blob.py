from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.blob import Blob


T = TypeVar("T", bound="ArticleFullTextContentBlob")


@_attrs_define
class ArticleFullTextContentBlob:
    """
    Attributes:
        file_data (Blob): Raw media bytes
    """

    file_data: Blob
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_data = self.file_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_data": file_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blob import Blob

        d = dict(src_dict)
        file_data = Blob.from_dict(d.pop("file_data"))

        article_full_text_content_blob = cls(
            file_data=file_data,
        )

        article_full_text_content_blob.additional_properties = d
        return article_full_text_content_blob

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
