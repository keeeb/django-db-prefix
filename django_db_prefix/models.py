from django.conf import settings
from django.db.models.signals import class_prepared, pre_init


def add_db_prefix(sender, **kwargs):
    prefix = getattr(settings, "DB_PREFIX", None)
    if prefix and not sender._meta.db_table.startswith(prefix) and getattr(sender, 'use_db_prefix', True):
        sender._meta.db_table = prefix + sender._meta.db_table


pre_init.connect(add_db_prefix)
class_prepared.connect(add_db_prefix)
