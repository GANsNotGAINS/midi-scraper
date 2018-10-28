# -*- coding: utf-8 -*-
import scrapy
import json

class MidiworldArtistsSpider(scrapy.Spider):
    name = 'midiworld_artists'
    allowed_domains = ['midiworld.com']
    start_urls = ['http://midiworld.com/composers.htm']

    def parse(self, response):
        urls = response.xpath('//blockquote//li/a/@href').extract()
        print(urls)
        with open("midiworld_artists.json", 'w') as f:
            json.dump(urls, f)