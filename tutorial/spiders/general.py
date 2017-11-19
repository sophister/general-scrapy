#! encoding:utf-8
import scrapy
import json
import codecs
import jsonpath_rw


class GeneralSpider(scrapy.Spider):
    name = "general"
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.8',
            'cache-control': 'no-cache',
            'cookie': 'cna=WscvEg7nMCECAXHQimpOzffc; v=0; cookie2=1acb0a3ece98f8b0e7d27ab42595d4d4; t=ed6a0349abc6bdf036c1f9505e1a5666; _tb_token_=e33b8e43867a5; rurl=aHR0cHM6Ly9wdWIuYWxpbWFtYS5jb20vaW5kZXguaHRt; undefined_yxjh-filter-1=true; isg=AsPDMWbwnSKIjVFW5YxLMJKsUoGtkJAdt8HG7vWjRyb4tObWfQvmyiFiUHMA',
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
        self.args = conf['args']
        self.conf = conf

    def start_requests(self):
        print self.base_url
        exit
        for i in self.args:
            url = self.base_url % tuple(i)
            yield scrapy.Request(url=url, callback=self.parse)

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
        print response.body
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
            
