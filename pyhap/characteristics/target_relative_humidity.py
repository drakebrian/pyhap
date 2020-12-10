# Autogenerated, do not edit. All changes will be undone.

from typing import List
from uuid import UUID

from pyhap.characteristic import (
    Characteristic,
    CharacteristicPermission,
)


class TargetRelativeHumidity(Characteristic):
    @property
    def characteristic_uuid(self) -> UUID:
        return UUID('00000034-0000-1000-8000-0026BB765291')

    @property
    def characteristic_type(self) -> str:
        return 'public.hap.characteristic.target.relative.humidity'

    @property
    def characteristic_format(self) -> str:
        return 'float'

    @property
    def permissions(self) -> List[CharacteristicPermission]:
        return [
            CharacteristicPermission.pair_read,
            CharacteristicPermission.pair_write,
            CharacteristicPermission.notify,
        ]
