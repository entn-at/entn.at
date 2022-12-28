AUTHOR = 'Ewald Enzinger'
SITENAME = 'entn.at'
SITESUBTITLE = "Ewald Enzinger's blog on ML, speech processing, and other research"
SITEURL = ''

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'America/Los_Angeles'

THEME = 'pelican-bootstrap3'

DEFAULT_LANG = 'en'
USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (('Forensic evaluation', 'http://forensic-evaluation.net/'),)
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/entn-at'),
          ('LinkedIn', 'https://linkedin.com/in/ewald-enzinger'),
          ('Twitter', 'https://twitter.com/entn_at'),)
          # ('Mastodon', 'https://sigmoid.social/entn_at'),)

DEFAULT_PAGINATION = 10

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

# Generate archive
ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

################## Add custom css #########################
# CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'CNAME', 'pdfs']
# EXTRA_PATH_METADATA = {'images/logo.png':{'path':'static/images/logo.png'},}

# Pelican Theme-Specific Variables
BOOTSTRAP_THEME = 'cosmo'#'sandstone'#'lumen'
SHOW_ARTICLE_CATEGORY = False
FEED_USE_SUMMARY = True
SUMMARY_MAX_LENGTH = 100
SHOW_ARTICLE_AUTHOR = False

SITELOGO = 'theme/images/logo.png'
SITELOGO_SIZE = 32
FAVICON = 'theme/images/logo.png'

ABOUT_ME = ""
AVATAR = ""
BANNER = "theme/images/banner.png"

DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
SHOW_ARTICLE_CATEGORY = True
TAG_CLOUD_MAX_ITEMS = 8

############################ Plugins ######################################
PLUGIN_PATHS = ['plugins']
PLUGINS = ['simple_footnotes']

PYGMENTS_STYLE = 'monokai'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
