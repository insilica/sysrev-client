from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event_types_items import WebhookEventTypesItems
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEndpoint")


@_attrs_define
class WebhookEndpoint:
    """This is an object representing a webhook endpoint.

    Attributes:
        id (str):  Example: we_1.
        created_at (int | Unset):
        event_types (list[WebhookEventTypesItems] | Unset): The list of event types that can be sent to this endpoint.
            ["*"] indicates all event types.
        owner_id (str | Unset): The ID of organization that the webhook endpoint belongs to. Example: org_1.
        updated_at (int | Unset):
        url (str | Unset):  Example: https://example.com/my_endpoint.
    """

    id: str
    created_at: int | Unset = UNSET
    event_types: list[WebhookEventTypesItems] | Unset = UNSET
    owner_id: str | Unset = UNSET
    updated_at: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = []
            for event_types_item_data in self.event_types:
                event_types_item = event_types_item_data.value
                event_types.append(event_types_item)

        owner_id = self.owner_id

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at", UNSET)

        _event_types = d.pop("event_types", UNSET)
        event_types: list[WebhookEventTypesItems] | Unset = UNSET
        if _event_types is not UNSET:
            event_types = []
            for event_types_item_data in _event_types:
                event_types_item = WebhookEventTypesItems(event_types_item_data)

                event_types.append(event_types_item)

        owner_id = d.pop("owner_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        webhook_endpoint = cls(
            id=id,
            created_at=created_at,
            event_types=event_types,
            owner_id=owner_id,
            updated_at=updated_at,
            url=url,
        )

        webhook_endpoint.additional_properties = d
        return webhook_endpoint

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
