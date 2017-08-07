import scrapy


class FirmsSpider(scrapy.Spider):
    name = "firms"

    allowed_domains = ["kostroma.orgdir.ru"]
    def start_requests(self):
        urls = [
            'https://kostroma.orgdir.ru/Мебель/?page=1/',
            'https://kostroma.orgdir.ru/Мебель/?page=2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'firms-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

