import scrapy
import json
import codecs


class QuotesSpider(scrapy.Spider):
    name = "taobao"
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.8',
            'cache-control': 'no-cache',
            'cookie': 'cna=WscvEg7nMCECAXHQimpOzffc; v=0; cookie2=1acb0a3ece98f8b0e7d27ab42595d4d4; t=ed6a0349abc6bdf036c1f9505e1a5666; _tb_token_=e33b8e43867a5; rurl=aHR0cHM6Ly9wdWIuYWxpbWFtYS5jb20vaW5kZXguaHRt; undefined_yxjh-filter-1=true; isg=AsPDMWbwnSKIjVFW5YxLMJKsUoGtkJAdt8HG7vWjRyb4tObWfQvmyiFiUHMA',
            'dnt': '1',
            'referer': 'https://pub.alimama.com/promo/search/index.htm?q=%E9%9E%8B&_t=1510473833209&toPage=2&perPageSize=50',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
    }

    def start_requests(self):
        base_url = 'https://pub.alimama.com/items/search.json?q=%E9%9E%8B&_t=1510473833209&perPageSize=50&auctionTag=&shopTag=yxjh&t=1510476145129&_tb_token_=e33b8e43867a5&pvid=10_221.219.205.151_377_1510474369752&toPage='
        for i in range(30):
            url = base_url + str(i + 1)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # filename = 'taobao.txt'
        # with open('taobao.txt', 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        # return
        json_body = json.loads(response.body)
        arr = json_body['data']['pageList']
        items = []
        for dict in arr:
            yield {
                'nick': dict['nick'],
                'pictUrl': dict['pictUrl']
            }
