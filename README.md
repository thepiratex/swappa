# Swappa Scraper (After-market Price Tracker)
A python program to fetch subscriptions from mail, pull the swappa listings (new and old), scrape them and do perform exploratory data analysis.

## What it helps with?
The after-market data can be used to understand the selling distribution and market trends before making a purchase

### Tools & Libraries Used
  1. [Python GMAIL API](https://developers.google.com/gmail/api/quickstart/python) - To read mails from GMAIL and fetch the listings for swappa
  2. [Scrapy](https://scrapy.org/) - To scrape data from swappa
  3. [Tableau](https://www.tableau.com/products/desktop) - To draw the visualization/EDA
  3. [Google Viz](https://developers.google.com/chart/interactive/docs/reference) - To draw visualization for the web (WIP)
 
 
### End Result 
 Data Info - 3000 listings (records)
 ---
### Which phone sells the most? (With median price sold in comparison to the prices not sold)

<img src="https://i.imgur.com/unH5iyg.png">

> iPhone 8 has 319 listings out of 3000 total. (Roughly 10% of total phones)
---
### Selling distribution of iPhone X (Sold vs Unsold)

<img src="https://i.imgur.com/gCOjvB9.png">

> For iPhone X, 400-470 price bin contains most of the phone which are listed as well as sold. One can see that prices above $570 are not being sold.

---
### Where are most sellers from?
<img src="https://i.imgur.com/8fOMIK0.png">
> New Jersey and Texas has the most sellers
