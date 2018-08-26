import scrapy




class LegalPersonsSpider(scrapy.Spider):
    name = "LegalPersons"
    start_urls = [
        # 'http://quotes.toscrape.com/tag/humor/',
        # 'https://sh.tianyancha.com/search/',
        'https://www.qichacha.com/g_SH_1.html',
    ]
    '''
        def parse(self, response):
            for searchlist in response.xpath('//section[@id="searchlist"]'):
                yield {
                     '公司名称': searchlist.css('a.span.span.name::text').extract_first(),
                    # '公司名称1': name.css('div.a.name::text').extract_first(),
                    # '法定代表人': content.css('info.title text-ellipsis.legalPersonName hover_underline::text').
                    # extract_first(),
                    # '联系方式': quote.css('span.text::text').extract_first(),
                }
            next_page = response.css('li.next a::attr("href")').extract_first()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
    '''


    def parse(self, response):
        yield {
        'Model':response.xpath('//div[@class="sb-list cp-list"]/dl/a/dd/text()').extract_first()
        }
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)