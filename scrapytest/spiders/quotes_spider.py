import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = "http://quotes.toscrape.com/"
        yield scrapy.Request(url,callback=self.parse)


    def parse(self, response):

        for text in response.css("div.quote"):

            yield  {
                "text":text.css("span.text::text").extract_first(),
                "author":text.css("small.author::text").extract_first(),
                "tag":text.css("a.tag::text").extract(),
            }
        nextPage = response.css("li.next a::attr(href)").extract_first()
        if nextPage is not None:
            yield scrapy.Request("http://quotes.toscrape.com/" + nextPage,callback=self.parse)


