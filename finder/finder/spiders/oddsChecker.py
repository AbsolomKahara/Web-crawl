import scrapy

class odds(scrapy.Spider):
	name='myOdds'
	start_urls=["http://fontfootball.blogspot.com/"]

	def parse(self,response):
		for item in response.xpath("//h3/a/text()"):
			print(item.getall())
	