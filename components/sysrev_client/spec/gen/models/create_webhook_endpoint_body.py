from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event_types_items import WebhookEventTypesItems

T = TypeVar("T", bound="CreateWebhookEndpointBody")


@_attrs_define
class CreateWebhookEndpointBody:
    """
    Attributes:
        event_types (list[WebhookEventTypesItems]): The list of event types that can be sent to this endpoint. ["*"]
            indicates all event types.
        owner_id (str): The ID of organization that the webhook endpoint belongs to. Example: org_1.
        url (str):  Example: https://example.com/my_endpoint.
    """

    event_types: list[WebhookEventTypesItems]
    owner_id: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_types = []
        for event_types_item_data in self.event_types:
            event_types_item = event_types_item_data.value
            event_types.append(event_types_item)

        owner_id = self.owner_id

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_types": event_types,
                "owner_id": owner_id,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_types = []
        _event_types = d.pop("event_types")
        for event_types_item_data in _event_types:
            event_types_item = WebhookEventTypesItems(event_types_item_data)

            event_types.append(event_types_item)

        owner_id = d.pop("owner_id")

        url = d.pop("url")

        create_webhook_endpoint_body = cls(
            event_types=event_types,
            owner_id=owner_id,
            url=url,
        )

        create_webhook_endpoint_body.additional_properties = d
        return create_webhook_endpoint_body

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
