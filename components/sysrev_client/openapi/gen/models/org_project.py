from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_project_admins_item import OrgProjectAdminsItem
    from ..models.project_settings import ProjectSettings


T = TypeVar("T", bound="OrgProject")


@_attrs_define
class OrgProject:
    """
    Attributes:
        project_id (str | Unset):  Example: proj_125327.
        name (str | Unset):
        member_count (int | Unset):
        last_active (str | Unset):
        settings (ProjectSettings | Unset):
        admins (list[OrgProjectAdminsItem] | Unset):
    """

    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    member_count: int | Unset = UNSET
    last_active: str | Unset = UNSET
    settings: ProjectSettings | Unset = UNSET
    admins: list[OrgProjectAdminsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        name = self.name

        member_count = self.member_count

        last_active = self.last_active

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        admins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.admins, Unset):
            admins = []
            for admins_item_data in self.admins:
                admins_item = admins_item_data.to_dict()
                admins.append(admins_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if member_count is not UNSET:
            field_dict["member_count"] = member_count
        if last_active is not UNSET:
            field_dict["last_active"] = last_active
        if settings is not UNSET:
            field_dict["settings"] = settings
        if admins is not UNSET:
            field_dict["admins"] = admins

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_project_admins_item import OrgProjectAdminsItem
        from ..models.project_settings import ProjectSettings

        d = dict(src_dict)
        project_id = d.pop("project_id", UNSET)

        name = d.pop("name", UNSET)

        member_count = d.pop("member_count", UNSET)

        last_active = d.pop("last_active", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: ProjectSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ProjectSettings.from_dict(_settings)

        _admins = d.pop("admins", UNSET)
        admins: list[OrgProjectAdminsItem] | Unset = UNSET
        if _admins is not UNSET:
            admins = []
            for admins_item_data in _admins:
                admins_item = OrgProjectAdminsItem.from_dict(admins_item_data)

                admins.append(admins_item)

        org_project = cls(
            project_id=project_id,
            name=name,
            member_count=member_count,
            last_active=last_active,
            settings=settings,
            admins=admins,
        )

        org_project.additional_properties = d
        return org_project

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
