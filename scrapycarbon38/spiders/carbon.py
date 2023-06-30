import scrapy


class CarbonSpider(scrapy.Spider):
    name = "carbon"
    allowed_domains = ["https://carbon38.com"]
    start_urls = ["https://www.carbon38.com/shop-all-activewear/tops"]

    def parse(self, response):
        
        yield {

            'breadcrumps':response.xpath("//a/text()").extract(),
            'image_url'  :response.xpath("//div[@class='AspectRatio.AspectRatio--withFallback']//img/src").extract(),
            'brand'     : response.css("div.ProductMeta a").xpath("@href").extract(),
            'product_name':response.xpath("//h1[@class='ProductMeta__Title Heading u-h3']/text()").extract(),
            'price':response.xpath("//span[@class='ProductMeta__Price Price']/text()").extract(),
            'reviews':response.xpath("//span[@class='yotpo-stars ']/text()").extract(),
            'colour' :response.xpath("//span[@class='ProductForm__SelectedValue ']/text()").extract(),
            'sizes'  :response.xpath("//label[@class='SizeSwatch']/text()").extract(),
            'description':response.xpath("//button[@class='Faq__Question u-h5']/text()").extract(),
        
        }

            
        