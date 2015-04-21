# coding: utf-8

"""A descriptor works only in a class.

We can store a different value for each instance in a dictionary
in the descriptor.
"""

from __future__ import print_function

from weakref import WeakKeyDictionary


class DescriptorWeakKeyDictStorage(object):
    """Descriptor that stores attribute data in instances.
    """
    _hidden = WeakKeyDictionary()

    def __init__(self, default=None):
        self.default = default

    def __get__(self, instance, owner):
        return DescriptorWeakKeyDictStorage._hidden.get(instance, self.default)

    def __set__(self, instance, value):
        DescriptorWeakKeyDictStorage._hidden[instance] = value


if __name__ == '__main__':
    class StoreInstance(object):
        """All instances have own `attr`.
        """
        attr = DescriptorWeakKeyDictStorage(10)

    store1 = StoreInstance()
    store2 = StoreInstance()
    print('store1', store1.attr)
    print('store2', store2.attr)
    print('Setting store1 only.')
    store1.attr = 100
    print('store1', store1.attr)
    print('store2', store2.attr)
    print('_hidden:', DescriptorWeakKeyDictStorage._hidden.items())
    del store1
    print('Deleted store1')
    print('_hidden:', DescriptorWeakKeyDictStorage._hidden.items())

