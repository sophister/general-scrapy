import scrapy
import json
import codecs


class QuotesSpider(scrapy.Spider):
    name = "stock50"
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.8',
            'cache-control': 'no-cache',
            'cookie': '',
            'dnt': '1',
            'referer': 'https://gupiao.baidu.com/stock/sh000016.html?from=aladingpc',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
    }

    def start_requests(self):
        base_url = 'https://gupiao.baidu.com/api/stocks/stockdaybar?from=pc&os_ver=1&cuid=xxx&vv=100&format=json&stock_code=sh%s&step=3&start=20170101&count=&fq_type=no&timestamp=1511068675871%s'
        args = [
            ["600000", ""],
            ["600029", ""],
            ["600048", ""],
            ["600104", ""],
            ["600485", ""],
            ["600547", ""],
            ["600887", ""],
            ["600999", ""],
            ["601166", ""],
            ["601198", ""],
            ["601288", ""],
            ["601336", ""],
            ["601601", ""],
            ["601688", ""],
            ["601800", ""],
            ["601881", ""],
            ["601988", ""],
            ["600016", ""],
            ["600030", ""],
            ["600050", ""],
            ["600111", ""],
            ["600518", ""],
            ["600606", ""],
            ["600919", ""],
            ["601006", ""],
            ["601169", ""],
            ["601211", ""],
            ["601318", ""],
            ["601390", ""],
            ["601628", ""],
            ["601766", ""],
            ["601818", ""],
            ["601901", ""],
            ["601989", ""],
            ["600028", ""],
            ["600036", ""],
            ["600100", ""],
            ["600340", ""],
            ["600519", ""],
            ["600837", ""],
            ["600958", ""],
            ["601088", ""],
            ["601186", ""],
            ["601229", ""],
            ["601328", ""],
            ["601398", ""],
            ["601668", ""],
            ["601788", ""],
            ["601857", ""],
            ["601985", ""]
        ]
        for i in args:
            url = base_url % tuple(i)
            yield scrapy.Request(url=url, callback=self.parse, meta={'code' : i[0]})

    def parse(self, response):
        meta = response.meta
        filename = './output-stock/' + meta['code'] + '.json'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        return
        # json_body = json.loads(response.body)
        # arr = json_body['data']['pageList']
        # items = []
        # for dict in arr:
        #     yield {
        #         'nick': dict['nick'],
        #         'pictUrl': dict['pictUrl']
        #     }
