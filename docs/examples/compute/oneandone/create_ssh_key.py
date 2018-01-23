import os

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

cls = get_driver(Provider.ONEANDONE)
drv = cls(key=os.environ.get('ONEANDONE_TOKEN'))

try:
    ssh_key = drv.ex_create_ssh_key(
        name="Test SSH Key",
        description=None,
        public_key=None
    )
    print(ssh_key)
except Exception as e:
    print(e)
