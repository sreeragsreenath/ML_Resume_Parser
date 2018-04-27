import scrapy
from scrapy.selector import Selector
import json
import re
import urllib.parse as urlparse
from scrapy.utils.project import get_project_settings
class IndeedSpider(scrapy.Spider):
    name = "indeed"

    

    def start_requests(self):
        position = self.position
        location = self.location
        position_text = position 
        position = position.replace(" ", "+")
        location = location.replace(" ", "%2C+")
        urls = [
            'https://www.indeed.com/jobs?q='+position+'&l='+location,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,  meta={'position': position_text})

    def parse(self, response):
        position = response.meta['position']
        jobs = response.css("div.result")
        print("Hello Sreerag look down")
        # print(jobs)
        for job in jobs:
            # print(job.css("a.jobtitle::attr(href)").extract())
            next_page = job.css("a.jobtitle::attr(href)").extract_first()
            next_page = response.urljoin(next_page)
            print(next_page)
            # print(next_page)
            yield scrapy.Request(url = next_page, callback=self.parsejob, meta={'position': position, 'job_page' : next_page})

    def parsejob(self, response):
        job_spec = response.css('title::text').extract()
        job_title = response.xpath("//b[@class = 'jobtitle']/font/text()").extract()
        job_desc = response.xpath("//table[@id = 'job-content']").css('td span').extract()
        company = re.sub("<.*?>", " ", str(job_desc[0]))
        job_desc = ''.join(job_desc)
        job_desc = re.sub("<.*?>", " ", str(job_desc))
        yield {
            'job_spec': job_spec,
            'job_title': job_title, 
            'job_desc' : job_desc,
            'position' : response.meta['position'],
            'job_page' : response.meta['job_page'],
            'company' : company
        }