#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Olin Gay'
SITENAME = 'Olin Gay - Blog'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Plugin configuration
PLUGINS = ['series']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
MY_EMAIL = "mailto:olin@olinbg.com"
MY_TWITTER = "http://twitter.com/olinbg"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
            ('email', MY_EMAIL),
		    ('twitter', MY_TWITTER),
            ('linkedin', 'http://linkedin.com/in/olinbg'),
            ('github', 'http://github.com/olinbg')
         )

DEFAULT_PAGINATION = 10

TEMPLATE_PAGES = {'admin/index.html': 'admin/index.html'}
STATIC_PATHS = ['images','files','favicon','admin']
ARTICLE_EXCLUDES = ['files','admin']
EXTRA_PATH_METADATA = {
    'files/github/.nojekyll': {'path': '.nojekyll'},
    'files/github/CNAME': {'path': 'CNAME'},
    'files/github/README.md': {'path': 'README.md'},
    # 'files/github/404.html': {'path': '404.html'},
    # 'files/robots.txt': {'path': 'robots.txt'},
}
THEME = 'hyde'
PROFILE_IMAGE = 'profile.jpg'

BIO = 'Putting it all together...<br /><br /><a href="/pages/about.html">About</a>'

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

CMS_ENV = "development"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
