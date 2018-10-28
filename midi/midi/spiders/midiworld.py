# -*- coding: utf-8 -*-
import scrapy
from midi.items import MidiItem

class MidiworldSpider(scrapy.Spider):
    name = 'midiworld'
    allowed_domains = ['midiworld.com']
    start_urls = [
        'http://www.midiworld.com/bach.htm',
        'http://www.midiworld.com/bartok.htm',
        'http://www.midiworld.com/beethoven.htm',
        'http://www.midiworld.com/brahms.htm',
        'http://www.midiworld.com/byrd.htm',
        'http://www.midiworld.com/chopin.htm',
        'http://www.midiworld.com/haydn.htm',
        'http://www.midiworld.com/handel.htm',
        'http://www.midiworld.com/hummel.htm',
        'http://www.midiworld.com/liszt.htm',
        'http://www.midiworld.com/mendelssohn.htm',
        'http://www.midiworld.com/mozart.htm',
        'http://www.midiworld.com/scarlatti.htm',
        'http://www.midiworld.com/schumann.htm',
        'http://www.midiworld.com/scriabin.htm',
        'http://www.midiworld.com/shostakovich.htm',
        'http://www.midiworld.com/tchaikovsky.htm',
        'http://www.midiworld.com/classic.htm'
    ]

    def parse(self, response):
        urls = response.xpath('//a/@href').extract()
        urls = filter(lambda x: x.endswith(".mid"), urls)
        urls = list(urls)

        yield MidiItem(
            file_urls=urls
        )