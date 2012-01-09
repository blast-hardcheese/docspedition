import urllib

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from docspedition.items import DocspeditionItem

class DocsPythonOrg(BaseSpider):
    name = "docs.python.org"
    allowed_domains = ["docs.python.org"]
    start_urls = [
        "http://docs.python.org/modindex.html",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        trs = hxs.select('//tr')

        items = []
        for tr in trs:
            tds = tr.select('./td')

            name = None
            link = "#"
            description = ""

            (_, nametd, descriptiontd,) = tds
            _name = nametd.select('./a/tt[@class="xref"]/text()').extract()
            _link = nametd.select('./a/@href').extract()
            _description = descriptiontd.select('./em/text()').extract()

            if not _name:
                continue

            assert len(_link) <= 1, "Malformed pydoc (too many links)"
            assert len(_description) <= 1, "Malformed pydoc (too many descriptions)"

            (name,) = _name

            if len(_link) == 1:
                (link,) = _link

            if len(_description) == 1:
                (description,) = _description

            item = DocspeditionItem()

            item['name'] = name
            item['link'] = urllib.basejoin(response.url, link)
            item['description'] = description

            items.append(item)
        return items
