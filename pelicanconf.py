#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

AUTHOR = 'Sarath Dontireddy'
SITENAME = 'silvderdreamracer.me'
SITETITLE = SITENAME
SITEURL = 'https://www.silverdreamracer.me'
SITESUBTITLE = '  You will Know it when i know it...'
PYGMENTS_STYLE = "monokai"
THEME = 'Flex'
STATIC_PATHS = ['images']
DATE_FORMATS = {
    "en": "%B %d, %Y",
}
FAVICON = '/images/favicon.ico'

PATH = 'content'

TIMEZONE = "America/New_York"

DEFAULT_LANG = 'en'
USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

BROWSER_COLOR = "#333"
ROBOTS = "index, follow"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

COPYRIGHT_YEAR = "2021  silverdreamracer.me"


# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
 #        ('Python.org', 'https://www.python.org/'),
  #       ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
   #      ('You can modify those links in your config file', '#'),)


# Social widget
SOCIAL = (('twitter', 'https://twitter.com/sarathreddy'),
          ('linkedin', 'https://www.linkedin.com/in/sarath-dontireddy/'),
          ('wordpress', 'https://spaceageracer.wordpress.com/'),
          ('github', 'https://github.com/sdontireddy'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = 'tags.html'


AUTHORS_BIO = {
  "sdontireddy": {
    "name": "Sarath Dontireddy",
    "cover": "https://media-exp1.licdn.com/dms/image/C4E03AQFjXy7HnxWZpA/profile-displayphoto-shrink_400_400/0/1523200602668?e=1630540800&v=beta&t=nl5vXtm7NgH90f-V9r0h79nZP3AZ-NXkEzxdBkmNrq4",
    "image": "https://media-exp1.licdn.com/dms/image/C4E03AQFjXy7HnxWZpA/profile-displayphoto-shrink_400_400/0/1523200602668?e=1630540800&v=beta&t=nl5vXtm7NgH90f-V9r0h79nZP3AZ-NXkEzxdBkmNrq4",
    "location": "Jacksonville, FL",
    "bio": "Computer Sceience Engr <p><img src=\'https://images.credly.com/size/680x680/images/2b31a8f4-92c4-468d-87eb-33115d97f6f5/AWS-DataAnalytics-Specialty-2020.png\' alt=\'Cert\'>AWS Certified Data Analytics  Specialty</p><p></p>",
    "linkedin": "sarath-dontireddy/",
    "github": "sdontireddy",
    "twitter": "sarathreddy",
  }
}


MENUITEMS = (
             ('Fork me on GitHub!', 'https://github.com/sdontireddy/silvderdreamracer.me'),
             ('Quick References', '/category/quick-reference'),
             ('AWS', '/category/aws')         
)


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}