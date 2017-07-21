import scrapy

from rt_crawler.items import RTItem

class RTSpider(scrapy.Spider):
    # spider name
    name = "RottenTomatoes"
    allowed_domains = ["rottentomatoes.com"]
    start_urls = [
        "https://www.rottentomatoes.com/top/bestofrt/?year=2017"
    ]
    
    def parse(self, response):
        for tr in response.xpath('//*[@id="top_movies_main"]/div/table/tr'):
            href = tr.xpath("./td[3]/a/@href")
            url = response.urljoin(href[0].extract())
            yield scrapy.Request(url, callback=self.parse_page_contents)

    def parse_page_contents(self, response):
        item = RTItem()
        item["title"] = response.xpath('//*[@id="heroImageContainer"]/a/h1/text()').extract()[0].strip()
        item["score"] = response.xpath('//*[@id="tomato_meter_link"]/span[2]/span/text()')[0].extract()
        yield item
        