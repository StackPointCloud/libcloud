import os

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

cls = get_driver(Provider.ONEANDONE)
drv = cls(key=os.environ.get('ONEANDONE_TOKEN'))

locations = drv.list_locations()

datacenter_es = [loc for loc in locations if loc.name == 'ES']

try:
    block_storage = drv.ex_create_block_storage(
        name="Test Block Storage", size=40,
        datacenter_id=datacenter_es[0].id,
        description=None, server_id=None
    )
    print(block_storage)
except Exception as e:
    print(e)
