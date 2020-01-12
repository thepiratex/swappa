def scrape():
    # -*- coding: utf-8 -*-
    import scrapy
    import pandas as pd
    from scrapy.crawler import CrawlerProcess
    import os
    
    if os.path.exists('output.csv'):
        os.remove('output.csv')

    class S1Spider(scrapy.Spider):
        name = 's1'
        allowed_domains = ['swappa.com']    
        urls = pd.read_csv("listings.csv")
        start_urls = urls

        def parse(self, response):
            url = response.request.url
            title = response.xpath('//h1/text()').extract_first().replace("\n",'').replace("\t",'')
            edition = response.xpath('//*[@id="section_top"]/div/div[1]/h1/small[1]/text()').extract_first()
            price = response.xpath('//*[@id="section_billboard"]/div/div[2]/div/div[1]/div[1]/div/span[2]/text()').extract_first()
            loc = response.xpath('//*[@id="section_billboard"]/div/div[1]/div/div/div[2]/ul/li/strong/text()').extract_first().replace("\n",'').replace("\t",'')
            platform = response.xpath('//*[@id="section_summary"]/div[1]/div[2]/div/div[1]/div/span[2]/text()').extract_first().replace("\n",'').replace("\t",'')
            if response.xpath('//*[@id="section_billboard"]/div/div[2]/div/div[1]/div[2]/div/text()').extract_first():
                state = response.xpath('//*[@id="section_billboard"]/div/div[2]/div/div[1]/div[2]/div/text()').extract_first().replace("\n",'').replace("\t",'')
            elif response.xpath('//*[@id="buy_now_btn"]/text()').extract_first():
                state = response.xpath('//*[@id="buy_now_btn"]/text()').extract_first().replace("\n",'').replace("\t",'')
            else:
                state = "NA"
            carrier = response.xpath('//*[@id="section_summary"]/div[1]/div[2]/div/div[2]/div/span[2]/text()').extract_first().replace("\n",'').replace("\t",'')
            color = response.xpath('//*[@id="section_summary"]/div[1]/div[2]/div/div[3]/div/span[2]/text()').extract_first().replace("\n",'').replace("\t",'')
            storage = response.xpath('//*[@id="section_summary"]/div[1]/div[2]/div/div[4]/div/span[2]/text()').extract_first().replace("\n",'').replace("\t",'')
            condition = response.xpath('//*[@id="section_summary"]/div[2]/div[1]/div[1]/span/text()').extract_first().replace("\n",'').replace("\t",'')
            listed_date = response.xpath('//*[@id="section_summary"]/div[3]/div[2]/div/div[1]/div/span[2]/text()').extract_first().replace("\n",'').replace("\t",'')
            views = response.xpath('//*[@id="section_summary"]/div[3]/div[2]/div/div[3]/div/span[2]/text()').extract_first().replace("\n",'').replace("\t",'')
            user = response.xpath('//*[@id="section_billboard"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/a/text()').extract_first().replace("\n",'').replace("\t",'')

            yield {
            'Product': title,
            'edition': edition,
            'price': price,
            'location':loc,
            'OS':platform,
            'state':state,
            'carrier': carrier,
            'color': color,
            'storage': storage,
            'condition': condition,
            'listed_date':listed_date,
            'views': views,
            'user': user,
            'url': url
            }


    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'output.csv' 
    })

    process.crawl(S1Spider)
    process.start()
