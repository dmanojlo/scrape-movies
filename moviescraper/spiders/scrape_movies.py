import scrapy
import random
import os

class TopRatedMovies(scrapy.Spider):

    name = 'top'

    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.jobId = kwargs.get('_job')
        print(self.jobId)

    start_urls = ['https://www.imdb.com/chart/top/']

    custom_settings = { 'FEEDS': {'/project/result.json': {'format': 'json', 'overwrite': True}}}

    def parse(self, response):
        a = random.randint(0,249)
        movie_name = response.css('.titleColumn a::text')[a].get()
        yield {'movie_name': movie_name, 'jobid': os.getcwd()}
