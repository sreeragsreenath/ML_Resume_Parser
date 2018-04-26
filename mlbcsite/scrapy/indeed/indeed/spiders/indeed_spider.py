import scrapy
from scrapy.selector import Selector
import json
import re

position = "data analyst"
location = "CA"
position = position.replace(" ", "+")
location = location.replace(" ", "%2C+")

class IndeedSpider(scrapy.Spider):
    name = "indeed"
    

    def start_requests(self):
        urls = [
            'https://www.indeed.com/jobs?q='+position+'&l='+location,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,  meta={'position': position})

    def parse(self, response):
        position = response.meta['position']
        jobs = response.css("div.result")
        print("Hello Sreerag look down")
        # print(jobs)
        for job in jobs:
            # print(job.css("a.jobtitle::attr(href)").extract())
            next_page = job.css("a.jobtitle::attr(href)").extract_first()
            next_page = response.urljoin(next_page)
            # print(next_page)
            yield scrapy.Request(url = next_page, callback=self.parsejob, meta={'position': position})

    def parsejob(self, response):
        job_spec = response.css('title::text').extract()
        job_title = response.xpath("//b[@class = 'jobtitle']/font/text()").extract()
        job_desc = response.xpath("//table[@id = 'job-content']").css('td span').extract()
        job_desc = ''.join(job_desc)
        job_desc = re.sub("<.*?>", " ", str(job_desc))
        yield {
            'job_spec': job_spec,
            'job_title': job_title, 
            'job_desc' : job_desc,
            'position' : response.meta['position'],
        }