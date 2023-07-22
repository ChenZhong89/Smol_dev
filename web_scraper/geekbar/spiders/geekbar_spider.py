```python
import scrapy
from scrapy.http import Request
from geekbar.items import GeekbarItem

class GeekbarSpider(scrapy.Spider):
    name = 'geekbar'
    allowed_domains = ['geekbar.com']
    start_urls = ['http://www.geekbar.com/product/list.html']

    def parse(self, response):
        products = response.xpath('//div[@class="product"]')
        for product in products:
            item = GeekbarItem()
            item['name'] = product.xpath('.//h2/a/text()').get()
            item['coil'] = product.xpath('.//div[@class="coil"]/text()').get()
            item['puff_count'] = product.xpath('.//div[@class="puff-count"]/text()').get()
            item['battery_specs'] = product.xpath('.//div[@class="battery-specs"]/text()').get()
            item['image_urls'] = product.xpath('.//img/@src').getall()
            yield item

        next_page = response.xpath('//a[@class="next-page"]/@href').get()
        if next_page is not None:
            yield Request(response.urljoin(next_page), callback=self.parse)
```