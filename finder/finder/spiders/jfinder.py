import scrapy
class findJob(scrapy.Spider):
	name='jobless'
	start_urls=["https://www.sunlitcentrekenya.co.ke/home/"]

	def parse(self,response):
		for j in response.css('div.section ol.jobs li.job'):
			print(j.css('dd.title a::text').get()+" : "+j.css('dd.location strong::text').get()+ " : "+j.css('dd.date strong::text').get())
			
		
		