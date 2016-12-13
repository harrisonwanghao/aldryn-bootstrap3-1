# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from .conf import settings


"""
Changable constants, overriden through settings
"""
# TODO make sure they are covered by README / Divio Cloud
GRID_SIZE = settings.ALDRYN_BOOTSTRAP3_GRID_SIZE


"""
Fixed constants, not influenced by settings
Changes here will most likely require database migrtions
"""
DEVICE_CHOICES = (
    ('xs', _('Tiny')),
    ('sm', _('Small')),
    ('md', _('Medium')),
    ('lg', _('Large')),
)

DEVICE_SIZES = tuple([size for size, name in DEVICE_CHOICES])

TARGET_CHOICES = (
    ('_blank', _('Open in new window')),
    ('_self', _('Open in same window')),
    ('_parent', _('Delegate to parent')),
    ('_top', _('Delegate to top')),
)

CONTEXT_CHOICES = (
    ('primary', 'Primary',),
    ('success', 'Success',),
    ('info', 'Info',),
    ('warning', 'Warning',),
    ('danger', 'Danger',),
)

CONTEXT_DEFAULT = 'default'

BUTTON_CONTEXT_CHOICES = (
    ('default', 'Default',),
) + CONTEXT_CHOICES + (
    ('link', 'Link',),
)

BUTTON_CONTEXT_DEFAULT = 'default'

TEXT_LINK_CONTEXT_CHOICES = (
    ('', 'Default',),
) + CONTEXT_CHOICES + (
    ('muted ', 'Muted',),
)

TEXT_LINK_CONTEXT_DEFAULT = ''

ASPECT_RATIOS = (
    (4, 3),
    (16, 9),
    (16, 10),
    (21, 9),
)

ASPECT_RATIOS_REVERSED = tuple([(y, x) for x, y in ASPECT_RATIOS])

ASPECT_RATIO_CHOICES = (
    tuple([
        ('{0}x{1}'.format(1, 1), '{0}x{1}'.format(1, 1))
    ]) + tuple([
        ('{0}x{1}'.format(x, y), '{0}x{1}'.format(x, y))
        for x, y in ASPECT_RATIOS
    ]) + tuple([
        ('{0}x{1}'.format(x, y), '{0}x{1}'.format(x, y))
        for x, y in ASPECT_RATIOS_REVERSED
    ]))

SIZE_CHOICES = (
    ('lg', _('Large'),),
    ('md', _('Medium'),),
    ('sm', _('Small'),),
    ('xs', _('Extra Small'),),
)

DEVICES = (
    {
        'identifier': 'xs',
        'name': _('Mobile phones'),
        'width': 768,
        'width_gutter': 750,
        'icon': 'mobile-phone',
    },
    {
        'identifier': 'sm',
        'name': _('Tablets'),
        'width': 768,
        'width_gutter': 750,
        'icon': 'tablet',
    },
    {
        'identifier': 'md',
        'name': _('Laptops'),
        'width': 992,
        'width_gutter': 970,
        'icon': 'laptop',
    },
    {
        'identifier': 'lg',
        'name': _('Large desktops'),
        'width': 1200,
        'width_gutter': 1170,
        'icon': 'desktop',
    },
)

for device in DEVICES:
    identifier = device['identifier']
    device['long_description'] = '{name} (<{width}px)'.format(**device)
    device['size_name'] = dict(SIZE_CHOICES).get(identifier)











SIZE_WIDGET_CHOICES = (
    # ('', 'Default'),
) + SIZE_CHOICES
SIZE_WIDGET_DEFAULT = 'md'

SIZES = tuple([size for size, name in SIZE_CHOICES])

SIZE_DEFAULT = 'md'

DEVICE_DICT = {device['identifier']: device for device in DEVICES}
