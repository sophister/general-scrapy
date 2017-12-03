# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'general'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}


IP_POOLS=[
    # {'ip': '118.144.149.200:3128'},
    # {'ip': '171.108.205.85:55555'},
    # {'ip': '111.155.116.227:8123'},
	# {'ip': '125.46.98.94:1920'},
    {'ip': '114.215.102.168:8081'},
    {'ip': '47.94.81.119:8888'},
    {'ip': '222.73.68.144:8090'},
    {'ip': '121.69.3.102:8080'},
    {'ip': '120.77.173.13:80'},
    {'ip': '106.14.51.145:8118'},
    {'ip': '120.237.91.34:9999'},
    {'ip': '58.22.61.211:3128'},
    {'ip': '39.108.171.142:80'},
    {'ip': '123.138.89.133:9999'},
    {'ip': '47.93.53.138:3128'},
    {'ip': '101.37.79.125:3128'},
    {'ip': '61.185.137.126:3128'},
    {'ip': '101.4.136.34:8080'},
    {'ip': '124.133.230.254:80'},
    {'ip': '121.196.226.246:84'},
    {'ip': '60.194.46.118:3128'},
    {'ip': '101.4.136.34:80'},
    {'ip': '101.4.136.34:81'},
    {'ip': '60.195.17.240:3128'},
    {'ip': '124.193.51.249:3128'},
    {'ip': '60.207.180.1:3128'},
    {'ip': '60.195.148.247:3128'},
    {'ip': '60.207.76.119:3128'},
    {'ip': '60.194.183.251:3128'},
    {'ip': '124.192.184.117:3128'},
    {'ip': '124.193.33.233:3128'},
    {'ip': '220.174.236.211:80'},
    {'ip': '124.192.39.248:3128'},
    {'ip': '60.194.46.119:3128'},
    {'ip': '113.200.214.164:9999'},
    {'ip': '111.13.109.27:80'},
    {'ip': '220.249.185.178:9797'},
    {'ip': '42.51.26.79:3128'},
    {'ip': '101.201.236.135:3128'},
    {'ip': '58.17.116.115:53281'},
    {'ip': '60.5.254.169:8081'},
    {'ip': '166.111.77.32:3128'},
    {'ip': '116.62.156.137:80'},
    {'ip': '112.114.98.40:8118'},
    {'ip': '47.94.230.42:9999'},
    {'ip': '220.197.176.26:8080'},
    {'ip': '180.173.149.123:9797'},
    {'ip': '27.213.254.198:8888'},
    {'ip': '223.215.181.112:808'},
    {'ip': '220.197.176.37:8080'},
    {'ip': '163.125.122.164:9999'},
    {'ip': '163.125.197.95:9797'},
    {'ip': '220.197.176.24:8080'},
    {'ip': '112.117.60.135:9999'},
    {'ip': '220.197.176.46:8080'},
    {'ip': '220.197.176.44:8080'},
    {'ip': '220.197.176.34:8080'},
    {'ip': '61.136.163.245:8103'},
    {'ip': '220.197.176.38:8080'},
    {'ip': '220.197.176.45:8080'},
    {'ip': '58.62.84.140:9999'},
    {'ip': '220.197.176.28:8080'},
    {'ip': '220.197.176.35:8080'},
    {'ip': '112.114.96.141:8118'},
    {'ip': '123.163.137.56:808'},
    {'ip': '222.71.121.248:31288'},
    {'ip': '61.163.138.189:9999'},
    {'ip': '220.197.176.22:8080'},
    {'ip': '223.240.210.79:808'},
    {'ip': '218.202.122.221:53281'},
    {'ip': '111.202.189.17:80'},
    {'ip': '220.197.176.48:8080'},
    {'ip': '182.88.149.11:9797'},
    {'ip': '112.95.207.96:8888'},
    {'ip': '101.68.73.54:53281'},
    {'ip': '183.51.191.21:9797'},
    {'ip': '106.42.97.33:808'},
    {'ip': '60.208.44.228:80'},
    {'ip': '58.16.42.224:80'},
    {'ip': '116.17.9.226:9999'},
    {'ip': '120.198.224.5:8080'},
    {'ip': '117.158.57.2:3128'},
    {'ip': '125.120.40.65:9999'},
    {'ip': '182.121.203.182:9999'},
    {'ip': '117.158.183.220:53281'},
    {'ip': '111.85.15.167:8080'},
    {'ip': '123.56.86.187:3128'},
    {'ip': '60.194.11.179:3128'},
    {'ip': '183.30.197.164:9797'},
    {'ip': '221.7.255.168:8080'},
    {'ip': '47.100.14.11:8080'},
    {'ip': '119.130.115.226:808'},
    {'ip': '47.95.244.122:3128'},
    {'ip': '112.74.217.34:80'},
    {'ip': '47.96.164.245:808'},
    {'ip': '14.221.164.246:9797'},
    {'ip': '60.215.200.160:8888'},
    {'ip': '171.37.31.151:9797'},
    {'ip': '221.7.255.167:8080'},
    {'ip': '39.108.6.49:3128'},
    {'ip': '120.32.208.19:8118'},
    {'ip': '122.72.108.53:80'},
    {'ip': '112.114.95.89:8118'},
    {'ip': '59.50.68.34:53281'}
]

USERAGENT_POOLS=[
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
]

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
    # 'tutorial.middlewares.IpPoolsMiddelware': 124,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 125,
    'tutorial.middlewares.UAPoolsMiddelware': 126
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
