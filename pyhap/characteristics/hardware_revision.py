# Autogenerated, do not edit. All changes will be undone.

from typing import (
    List,
    Type,
)
from uuid import UUID

from pyhap.characteristic import (
    Characteristic,
    CharacteristicPermission,
)


class HardwareRevision(Characteristic):
    @property
    def characteristic_uuid(self) -> UUID:
        return UUID('00000053-0000-1000-8000-0026BB765291')

    @property
    def characteristic_type(self) -> Type:
        return str

    @property
    def characteristic_format(self) -> str:
        return 'string'

    @property
    def permissions(self) -> List[CharacteristicPermission]:
        return [
            CharacteristicPermission.pair_read,
        ]
