#! encoding:utf-8
import scrapy
import json
import codecs
import jsonpath_rw
import logging


class GeneralSpider(scrapy.Spider):
    name = "general"
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.8',
            'cache-control': 'no-cache',
            'dnt': '1',
            'referer': '',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
    }

    def __init__(self, config=None):
        with open(config, "r") as f:
            content = f.read()
        conf = json.loads(content)
        #type: json/jsonp/html
        self.crawl_type = conf['crawl_type']
        self.base_url = conf['base_url']
        self.conf = conf

        # 添加自定义header
        if 'request_headers' in conf:
            self.custom_settings['DEFAULT_REQUEST_HEADERS'] = conf['request_headers']

    def start_requests(self):
        if 'args' in self.conf:
            url_list = self.handle_args_requests()
        else:
            url_list = [self.base_url]

        url_all = []

        if 'range' in self.conf:
            for url in url_list:
                new_url_list = self.handle_range_requests(url, self.conf['range'])
                url_all.extend(new_url_list)
        else:
            url_all = url_list
        # logging.debug("url list is: ")
        # logging.debug(url_all)
        
        return [scrapy.Request(url=url, callback=self.parse) for url in url_all]
        
    #处理用户提供了所有的页面循环值
    def handle_args_requests(self):
        out = []
        for i in self.conf['args']:
            url = self.base_url % tuple(i)
            out.append(url)
            # out.append(scrapy.Request(url=url, callback=self.parse))
        return out

    #处理用户只提供了 起始值，结束值，步进 的情况
    def handle_range_requests(self, url, page_range):
        out = []
        for page in xrange(*page_range):
            new_url = url
            new_url = new_url.replace('#page#', str(page))
            out.append(new_url)
        return out

    def parse(self, response):
        # filename = 'taobao.txt'
        # with open('taobao.txt', 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        # return
        if self.crawl_type == "html":
            obj = self.handleHTML(response)
            yield obj
        else:
            if self.crawl_type == "jsonp":
                content = response.body.strip()
                content = content[1+len(self.conf['jsonp_callback']):-2]
            else:
                content = response.body
            json_body = json.loads(content)
            arr = self.handleResponse(json_body)
            for i in arr:
                yield i

    def handleResponse(self, obj):
        jsonpath_expr = jsonpath_rw.parse(self.conf['list_json_path'])
        arr = [match.value for match in jsonpath_expr.find(obj)]
        out = []
        if 'output_item' in self.conf:
            for i in arr:
                temp = {}
                for from_key,to_key in self.conf['output_item'].items():
                    if from_key in i :
                        temp[to_key] = i[from_key]
                out.append(temp)
        else:
            out = arr
        return out
    
    def handleHTML(self, response):
        
        out = {}

        if 'output_item' in self.conf:
            for to_key, from_path in self.conf['output_item'].items():
                out[to_key] = response.xpath(from_path).extract_first()

        if 'output_list' in self.conf:
            for i in self.conf['output_list']:
                out[i['output_key']] = []
                
                for item in response.xpath(i['list_path']):
                    obj = {}
        
                    for to_key, from_path in i['items'].items():
                        
                        obj[to_key] = item.xpath(from_path).extract_first()
                    out[i['output_key']].append(obj)

        return out
            
