# -*- coding: utf-8 -*-
import scrapy

import zlib

import configs

class AlbumSpider(scrapy.Spider):
    name = 'album_spider'

    def start_requests(self):
        base_url = 'https://api.deezer.com/album/'
        for i in xrange(100000, 100050):
            url = base_url + str(i)
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        data = response.body
        if response.headers.has_key('Content-Encoding') and response.headers['Content-Encoding'] == 'gzip':
            data = zlib.decompress(data, 16+zlib.MAX_WBITS)
        yield {'album': data}


    @property
    def headers(self):
        return configs.config.headers
