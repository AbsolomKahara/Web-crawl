import scrapy
class findJob(scrapy.Spider):
	name="odds"
	start_urls=["https://www.oddschecker.com/football/english/premier-league/watford-v-arsenal/winner"]

	def parse(self,response):
		for j in response.css('div.outerWrapperClass_o1k614qs OuterWrapper_o14fy1qi div.scrollingClass_s1czl3rd innerWrapperClass_iyj238m'):
			print(j.css('div.BookmakersRowOuterWrapper_b1pfx62b div.bookmakersRowWrapper_b6m3edq RowLayout_refg9ta a::attr(title)').get())
			
		
		