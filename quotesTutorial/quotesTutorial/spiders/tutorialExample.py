import scrapy
class jobs(scrapy.Spider):
	name='myjobs'
	#job_urls='https://www.myjobsinkenya.com/'
	start_urls=["https://jobupdatesconnections.co.ke/"]

	def parse(self, response):
		for job in response.css('li.post-3444 job_listing type-job_listing status-publish has-post-thumbnail hentry job-type-full-time-jobs'):
			print(job.css('div.position ::text').get())
		
	
