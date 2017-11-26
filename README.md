# general-scrapy
general scrapy for json/jsonp/html crawl

## 依赖:

* `python`: 2.7.14
* `scrapy`: 1.3.3
* `jsonpath_rw`: 1.4.0


## how to run

```shell
# 抓取JSONP数据源
scrapy crawl general -a config=config/jsonp-demo.json -o test2.json
# 对API接口的 args 支持
scrapy crawl general -a config=config/api-demo.json -o test.json
# 对API接口的 range范围 支持
scrapy crawl general -a config=config/api-range-demo.json -o test-range.json
# html 静态页面
scrapy crawl general -a config=config/html-demo.json -o test3.json
# 登录态验证
scrapy crawl general -a config=config/github-login-demo.json -o test-login.json
```