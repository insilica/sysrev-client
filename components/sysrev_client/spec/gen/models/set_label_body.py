from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_settings import LabelSettings
    from ..models.set_label_body_schema_type_0 import SetLabelBodySchemaType0


T = TypeVar("T", bound="SetLabelBody")


@_attrs_define
class SetLabelBody:
    """
    Attributes:
        settings (LabelSettings | Unset):
        schema (None | SetLabelBodySchemaType0 | str | Unset):
    """

    settings: LabelSettings | Unset = UNSET
    schema: None | SetLabelBodySchemaType0 | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.set_label_body_schema_type_0 import SetLabelBodySchemaType0

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        schema: dict[str, Any] | None | str | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, SetLabelBodySchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_settings import LabelSettings
        from ..models.set_label_body_schema_type_0 import SetLabelBodySchemaType0

        d = dict(src_dict)
        _settings = d.pop("settings", UNSET)
        settings: LabelSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = LabelSettings.from_dict(_settings)

        def _parse_schema(data: object) -> None | SetLabelBodySchemaType0 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = SetLabelBodySchemaType0.from_dict(data)

                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SetLabelBodySchemaType0 | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        set_label_body = cls(
            settings=settings,
            schema=schema,
        )

        set_label_body.additional_properties = d
        return set_label_body

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
