import scrapy

from scrapy.loader import ItemLoader
from ..items import BulgramItem


class BulgramSpider(scrapy.Spider):
	name = 'bulgram'
	start_urls = ['https://www.bulgram.com/cat/5/%D0%9D%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8.html']

	def parse(self, response):
		post_links = response.xpath('//div[@class="single_post"]/a/@href')

		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="col-md-12 col-xs-12"]/descendant-or-self::*/text()[normalize-space() and not(ancestor::a | ancestor::script | ancestor::style)]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description)
		date = response.xpath('//p[@style="float: left;"]/text()').get().strip()

		item = ItemLoader(item=BulgramItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()