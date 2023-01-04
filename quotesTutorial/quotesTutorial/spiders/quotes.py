import scrapy

class QuotesTutorial(scrapy.Spider):
	name= 'Quote'
	start_urls=['https://quotes.toscrape.com/']

	def parse(self,response):
		h1_tag=response.xpath('//h1/a/text()').getall()
		tags=response.xpath('//*[@class="tag-item"]/a/text()').getall()

		yield {'H1 Tag' :h1_tag,'Tags':tags}