#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aaron Kitzmiller'
SITENAME = '@HouseBoyCoder'
SITEURL = ''
THEME = 'theme'
PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Harvard FAS Informatics', 'https://informatics.fas.harvard.edu/'),
    ('FAS Research Computing', 'https://rc.fas.harvard.edu'),
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/HouseBoyCoder'),
    ('github', 'https://github.com/aaronk'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images']

