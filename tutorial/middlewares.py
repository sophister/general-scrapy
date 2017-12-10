# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import random
import logging
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.core.downloader.handlers.http11 import TunnelError
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware #代理UA，固定导入
import settings
import requests

class IpPoolsMiddelware(HttpProxyMiddleware):

    def __init__(self,ip=''):
        self.service = settings.PROXY_SERVICE
        self.https_proxy_list = []
        self.http_proxy_list = []
        self.ip = ip
        self.update_count = 100

    def process_request(self, request, spider):
        if request.url.find('https://') == 0:
            proxy_list = self.get_https_proxy()
        else:
            proxy_list = self.get_http_proxy()

        if not proxy_list:
            return

        proxy = random.choice(proxy_list)
        ip_port = "http://%s:%s" % (proxy[0], proxy[1])
        request.meta["proxy"] = ip_port
        logging.debug('current proxy is:' + ip_port)

    def get_http_proxy(self):
        proxy_list = self.get_proxy(0)
        if proxy_list:
            self.http_proxy_list = proxy_list

        return self.http_proxy_list

    def get_https_proxy(self):
        proxy_list = self.get_proxy(1)
        if proxy_list:
            self.https_proxy_list = proxy_list

        return self.https_proxy_list

    def get_proxy(self, protocol):
        proxy_list = []
        if self.update_count >= 100:
            self.update_count = 0 
            url = self.service + '/?types=0&protocol=' + str(protocol) +'&count=50&country=国内'
            r = requests.get(self.service)
            if r.status_code == 200:
                proxy_list = r.json()
        self.update_count += 1
        return proxy_list


class UAPoolsMiddelware(UserAgentMiddleware):
    def __init__(self, ua=''):
        self.user_agent = ua
        self.user_agent_pools = settings.USERAGENT_POOLS

    def process_request(self, request, spider):
        '''使用代理UA，随机选用'''
        ua = random.choice(self.user_agent_pools)
        logging.debug('current user-agent: ' + ua)
        try:
            request.headers.setdefault('User-Agent',ua)
        except Exception,e:
            print e
            pass
    

class TutorialSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
