import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='td[7]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}

        item['name'] = response.xpath('//*[@id="player_offense"]/tbody/tr/th/a/text()').getall()
        item['passing']['touchdown'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[5]/text()').getall()
        item['passing']['yards'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[4]/text()').getall()
        item['passing']['attempted'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[3]/text()').getall()
        item['passing']['completed'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[2]/text()').getall()
        item['passing']['rating'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[10]/text()').getall()
        item['rushing']['touchdown'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[13]/text()').getall()
        item['rushing']['yards'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[12]/text()').getall()
        item['receiving']['touchdown'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[18]/text()').getall()
        item['receiving']['yards'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[17]/text()').getall()
        item['receiving']['targets'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[15]/text()').getall()
        item['receiving']['Recorded'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[16]/text()').getall()
        item['team']['name'] = response.xpath('//*[@id="player_offense"]/tbody/tr/td[1]/text()').getall()
        print(item)
        return item
