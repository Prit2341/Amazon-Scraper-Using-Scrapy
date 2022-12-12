import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        "https://www.amazon.in/Cosmic-Byte-CB-GK-26-Mechanical-Keyboard/dp/B09MR4SYZF/ref=d_pd_sbs_sccl_3_3/257-1559153-4504332?pd_rd_w=jiukx&content-id=amzn1.sym.e2ce9e2f-6d12-4c08-abc6-a5b1e7e9208f&pf_rd_p=e2ce9e2f-6d12-4c08-abc6-a5b1e7e9208f&pf_rd_r=Z0S01FKXNBZJ116X7WW6&pd_rd_wg=3nAIA&pd_rd_r=701b4d5c-dd04-4b64-b193-d033f16f5882&pd_rd_i=B09MR4SYZF&th=1"
        ]

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('#productTitle::text').extract()
        product_price = response.css('.priceToPay span').css('::text').get()
        product_desc = response.css("#feature-bullets .a-list-item").css('::text').extract()
        product_rating = response.css('#reviewsMedley .a-size-medium').css('::text').get()
        product_indetail_review = response.css('#cm-cr-dp-review-list .a-text-bold span').css('::text').extract()

        
        
        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_rating'] = product_rating
        items['product_dec'] = product_desc
        items['product_indetali_review'] = product_indetail_review

        yield items