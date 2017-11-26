# general-scrapy
general scrapy for json/jsonp/html crawl

## how to run

```shell
# 抓取JSONP数据源
scrapy crawl general -a config=config/jsonp-demo.json -o test2.json
# 对range范围的支持
scrapy crawl general -a config=config/api-range-demo.json -o test-range.json
# html
scrapy crawl general -a config=config/html-demo.json -o test3.json
# 登录态验证
scrapy crawl general -a config=config/github-login-demo.json -o test-login.json
```