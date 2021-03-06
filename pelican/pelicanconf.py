#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'alex thompson'
SITENAME = 'Resume of Alex Thompson'
SITEURL = 'https://alex1412108.github.io'

PATH = 'content'

OUTPUT_PATH = '../'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

THEME = 'notmyidea'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/alex-thompson-47a9aa48/'),
          ('github', 'https://github.com/alex1412108'),)

DEFAULT_PAGINATION = False

TYPOGRIFY = True
SLUGIFY_SOURCE = 'basename'
NEWEST_FIRST_ARCHIVES = True
ARTICLE_ORDER_BY = 'reversed-date'
GITHUB_URL = 'https://github.com/alex1412108'
GOOGLE_ANALYTICS = 'UA-89119637-1'


#uncomment the following line if you want to adjust the social widget name
#SOCIAL_WIDGET_NAME = ''

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
