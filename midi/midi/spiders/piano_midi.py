# -*- coding: utf-8 -*-
import scrapy
from midi.items import MidiItem

class PianoMidiSpider(scrapy.Spider):
    name = 'piano-midi'
    allowed_domains = ['piano.midi.de']
    start_urls = [
                    'http://www.piano-midi.de/albeniz.htm', 
                    'http://www.piano-midi.de/bach.htm', 
                    'http://www.piano-midi.de/balak.htm', 
                    'http://www.piano-midi.de/beeth.htm', 
                    'http://www.piano-midi.de/borodin.htm', 
                    'http://www.piano-midi.de/brahms.htm', 
                    'http://www.piano-midi.de/burgm.htm', 
                    'http://www.piano-midi.de/chopin.htm', 
                    'http://www.piano-midi.de/clementi.htm', 
                    'http://www.piano-midi.de/debuss.htm', 
                    'http://www.piano-midi.de/godowsky.htm', 
                    'http://www.piano-midi.de/grana.htm', 
                    'http://www.piano-midi.de/grieg.htm', 
                    'http://www.piano-midi.de/haydn.htm', 
                    'http://www.piano-midi.de/liszt.htm', 
                    'http://www.piano-midi.de/mendelssohn.htm', 
                    'http://www.piano-midi.de/moszkowski.htm', 
                    'http://www.piano-midi.de/mozart.htm', 
                    'http://www.piano-midi.de/muss.htm', 
                    'http://www.piano-midi.de/rach.htm', 
                    'http://www.piano-midi.de/ravel.htm', 
                    'http://www.piano-midi.de/schub.htm', 
                    'http://www.piano-midi.de/schum.htm', 
                    'http://www.piano-midi.de/sinding.htm', 
                    'http://www.piano-midi.de/tschai.htm'
                ]


    def parse(self, response):
        urls = response.xpath('//td[contains(@class, "midi")]//a[contains(@class, "navi")]/@href').extract()
        urls = filter(lambda x: x.endswith(".mid"), urls)
        urls = list(urls)
        urls = list(map(lambda x: 'http://www.piano-midi.de/' + x, urls))

        yield MidiItem(
            file_urls=urls
        )



