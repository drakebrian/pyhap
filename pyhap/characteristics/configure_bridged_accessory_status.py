# Autogenerated, do not edit. All changes will be undone.

from typing import List
from uuid import UUID

from pyhap.characteristic import (
    Characteristic,
    CharacteristicPermission,
)


class ConfigureBridgedAccessoryStatus(Characteristic):
    @property
    def characteristic_uuid(self) -> UUID:
        return UUID('0000009D-0000-1000-8000-0026BB765291')

    @property
    def characteristic_type(self) -> str:
        return 'public.hap.characteristic.configure.bridged.accessory.status'

    @property
    def characteristic_format(self) -> str:
        return 'tlv'

    @property
    def permissions(self) -> List[CharacteristicPermission]:
        return [
            CharacteristicPermission.pair_read,
            CharacteristicPermission.notify,
        ]
