from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_export_status import ProjectExportStatus
from ..models.project_export_type import ProjectExportType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectExport")


@_attrs_define
class ProjectExport:
    """This is an object representing a project export.

    Attributes:
        id (str):  Example: project_export_1.
        created_at (int | Unset):
        download_url (str | Unset): The URL to download the export.
        export_type (ProjectExportType | Unset):
        status (ProjectExportStatus | Unset):
    """

    id: str
    created_at: int | Unset = UNSET
    download_url: str | Unset = UNSET
    export_type: ProjectExportType | Unset = UNSET
    status: ProjectExportStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        download_url = self.download_url

        export_type: str | Unset = UNSET
        if not isinstance(self.export_type, Unset):
            export_type = self.export_type.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if export_type is not UNSET:
            field_dict["export_type"] = export_type
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at", UNSET)

        download_url = d.pop("download_url", UNSET)

        _export_type = d.pop("export_type", UNSET)
        export_type: ProjectExportType | Unset
        if isinstance(_export_type, Unset):
            export_type = UNSET
        else:
            export_type = ProjectExportType(_export_type)

        _status = d.pop("status", UNSET)
        status: ProjectExportStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProjectExportStatus(_status)

        project_export = cls(
            id=id,
            created_at=created_at,
            download_url=download_url,
            export_type=export_type,
            status=status,
        )

        project_export.additional_properties = d
        return project_export

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
