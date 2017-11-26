# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import random
import logging
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware #代理ip，这是固定的导入
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware #代理UA，固定导入
import settings

class IpPoolsMiddelware(HttpProxyMiddleware):

    def __init__(self,ip=''):
        self.ip_pools = settings.IP_POOLS
        self.ip = ip

    def process_request(self, request, spider):
        ip = random.choice(self.ip_pools)
        logging.debug('current proxy ip: '+ip['ip'])
        try:
            request.meta["proxy"] = "http://"+ip['ip']
        except Exception,e:
            print e
            pass

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
