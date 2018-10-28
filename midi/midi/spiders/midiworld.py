# -*- coding: utf-8 -*-
import scrapy
from midi.items import MidiItem

class MidiworldSpider(scrapy.Spider):
    name = 'midiworld'
    allowed_domains = ['midiworld.com']
    start_urls = ['http://www.midiworld.com/classic.htm']

    def parse(self, response):
        urls = response.xpath('//b//a/@href').extract()
        urls = filter(lambda x: x.endswith(".mid"), urls)
        urls = list(urls)

        yield MidiItem(
            file_urls=urls
        )