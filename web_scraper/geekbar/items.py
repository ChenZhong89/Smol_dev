```python
import scrapy

class GeekbarItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    coil = scrapy.Field()
    puff_count = scrapy.Field()
    battery_specs = scrapy.Field()
    product_photo = scrapy.Field()
```