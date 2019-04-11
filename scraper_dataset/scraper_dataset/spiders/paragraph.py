import scrapy

class ParagraphSpider(scrapy.Spider):
    name = "paragraph"

    start_urls = [
        'https://www.republika.co.id/index/internasional/2019/01/01',
        'https://www.republika.co.id/index/internasional/2019/01/02',
        'https://www.republika.co.id/index/internasional/2019/01/03',
        'https://www.republika.co.id/index/internasional/2019/01/04',
        'https://www.republika.co.id/index/internasional/2019/01/05',
        'https://www.republika.co.id/index/internasional/2019/01/06',
        'https://www.republika.co.id/index/internasional/2019/01/07',
        'https://www.republika.co.id/index/internasional/2019/01/08',
        'https://www.republika.co.id/index/internasional/2019/01/09',
        'https://www.republika.co.id/index/internasional/2019/01/10',
        'https://www.republika.co.id/index/internasional/2019/01/11',
        'https://www.republika.co.id/index/internasional/2019/01/12',
        'https://www.republika.co.id/index/internasional/2019/01/13',
        'https://www.republika.co.id/index/internasional/2019/01/14',
        'https://www.republika.co.id/index/internasional/2019/01/15',
        'https://www.republika.co.id/index/internasional/2019/01/16',
        'https://www.republika.co.id/index/internasional/2019/01/17',
        'https://www.republika.co.id/index/internasional/2019/01/18',
        'https://www.republika.co.id/index/internasional/2019/01/19',
        'https://www.republika.co.id/index/internasional/2019/01/20',
        'https://www.republika.co.id/index/internasional/2019/01/21',
        'https://www.republika.co.id/index/internasional/2019/01/22',
        'https://www.republika.co.id/index/internasional/2019/01/23',
        'https://www.republika.co.id/index/internasional/2019/01/24',
        'https://www.republika.co.id/index/internasional/2019/01/25',
        'https://www.republika.co.id/index/internasional/2019/01/26',
        'https://www.republika.co.id/index/internasional/2019/01/27',
        'https://www.republika.co.id/index/internasional/2019/01/28',
        'https://www.republika.co.id/index/internasional/2019/01/29',
        'https://www.republika.co.id/index/internasional/2019/01/30',
        'https://www.republika.co.id/index/internasional/2019/01/31',
        'https://www.republika.co.id/index/ekonomi/2019/01/01',
        'https://www.republika.co.id/index/ekonomi/2019/01/02',
        'https://www.republika.co.id/index/ekonomi/2019/01/03',
        'https://www.republika.co.id/index/ekonomi/2019/01/04',
        'https://www.republika.co.id/index/ekonomi/2019/01/05',
        'https://www.republika.co.id/index/ekonomi/2019/01/06',
        'https://www.republika.co.id/index/ekonomi/2019/01/07',
        'https://www.republika.co.id/index/ekonomi/2019/01/08',
        'https://www.republika.co.id/index/ekonomi/2019/01/09',
        'https://www.republika.co.id/index/ekonomi/2019/01/10',
        'https://www.republika.co.id/index/ekonomi/2019/01/11',
        'https://www.republika.co.id/index/ekonomi/2019/01/12',
        'https://www.republika.co.id/index/ekonomi/2019/01/13',
        'https://www.republika.co.id/index/ekonomi/2019/01/14',
        'https://www.republika.co.id/index/ekonomi/2019/01/15',
        'https://www.republika.co.id/index/ekonomi/2019/01/16',
        'https://www.republika.co.id/index/ekonomi/2019/01/17',
        'https://www.republika.co.id/index/ekonomi/2019/01/18',
        'https://www.republika.co.id/index/ekonomi/2019/01/19',
        'https://www.republika.co.id/index/ekonomi/2019/01/20',
        'https://www.republika.co.id/index/ekonomi/2019/01/21',
        'https://www.republika.co.id/index/ekonomi/2019/01/22',
        'https://www.republika.co.id/index/ekonomi/2019/01/23',
        'https://www.republika.co.id/index/ekonomi/2019/01/24',
        'https://www.republika.co.id/index/ekonomi/2019/01/25',
        'https://www.republika.co.id/index/ekonomi/2019/01/26',
        'https://www.republika.co.id/index/ekonomi/2019/01/27',
        'https://www.republika.co.id/index/ekonomi/2019/01/28',
        'https://www.republika.co.id/index/ekonomi/2019/01/29',
        'https://www.republika.co.id/index/ekonomi/2019/01/30',
        'https://www.republika.co.id/index/ekonomi/2019/01/31',
    ]

    def parse(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first()

        # follow links to product pages
        for href in response.css('div.txt_subkanal.txt_index h2 a::attr(href)'):
            yield response.follow(href, self.parse_product)

        # follow pagination links
        # for href in response.css('a.ant-pagination-item-link::attr(href)'):
        #     yield response.follow(href, self.parse)

    def parse_product(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first()

        yield {
            'content': response.css('div.artikel p::text').extract(),
        }