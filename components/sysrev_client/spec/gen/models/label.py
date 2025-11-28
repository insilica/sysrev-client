from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_schema_type_0 import LabelSchemaType0
    from ..models.label_settings import LabelSettings


T = TypeVar("T", bound="Label")


@_attrs_define
class Label:
    """
    Example:
        {'id': 'label_1', 'schema': {'type': 'boolean', 'title': 'Include', 'description': 'Include this article?'}}

    Attributes:
        id (str):  Example: label_1.
        settings (LabelSettings | Unset):
        schema (LabelSchemaType0 | None | str | Unset):
    """

    id: str
    settings: LabelSettings | Unset = UNSET
    schema: LabelSchemaType0 | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.label_schema_type_0 import LabelSchemaType0

        id = self.id

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        schema: dict[str, Any] | None | str | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, LabelSchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if settings is not UNSET:
            field_dict["settings"] = settings
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_schema_type_0 import LabelSchemaType0
        from ..models.label_settings import LabelSettings

        d = dict(src_dict)
        id = d.pop("id")

        _settings = d.pop("settings", UNSET)
        settings: LabelSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = LabelSettings.from_dict(_settings)

        def _parse_schema(data: object) -> LabelSchemaType0 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = LabelSchemaType0.from_dict(data)

                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LabelSchemaType0 | None | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        label = cls(
            id=id,
            settings=settings,
            schema=schema,
        )

        label.additional_properties = d
        return label

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
