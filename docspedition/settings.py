# Scrapy settings for docspedition project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'docspedition'
BOT_VERSION = '0.1'

SPIDER_MODULES = ['docspedition.spiders']
NEWSPIDER_MODULE = 'docspedition.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

