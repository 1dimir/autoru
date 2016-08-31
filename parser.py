#!/usr/local/env python
# -*- coding: utf-8 -*-

from lxml import etree
from lxml.etree import HTMLParser



def get_value(document_tree, xpath):
    result = document_tree.xpath(xpath)
    if result:
        return result[0].strip()
    else:
        return None


class SearchItem(object):


    def __init__(self, document_tree=None):
        self.year = ''
        self.mileage = ''
        self.description = ''
        self.price = ''
        self.currency = ''
        self.url = ''
        self.model = ''

        if not document_tree is None:
            self.parse(document_tree)


    def parse(self, document_tree):
        self.year = get_value(document_tree, './/div[contains(@class, \'listing-item__year\')]/text()')
        self.mileage = get_value(document_tree, './/div[contains(@class, \'listing-item__km\')]/text()')
        self.description = get_value(document_tree, './/div[contains(@class, \'listing-item__description\')]/text()')
        self.price = get_value(document_tree, './/div[contains(@class, \'listing-item__price\')]/text()')
        self.currency = get_value(document_tree, './/div[contains(@class, \'listing-item__price\')]'
            '/div[contains(@class, \'i-currency-symbol__seo-currency\')]/text()')
        self.url = get_value(document_tree, './/a[contains(@class, \'listing-item__link\')]/@href')
        self.model = get_value(document_tree, './/a[contains(@class, \'listing-item__link\')]/text()') + \
            ' ' + \
            get_value(document_tree, './/span[contains(@class, \'listing-item__avtokod\')]/text()')

class SearchList(object):

    def __init__(self, document_tree=None):
        if not tree is None:
            self.items = [
                SearchItem(x) for x in document_tree.xpath('//tbody[contains(@class, \'listing-item\')'
                                 'and @data-bem]')
            ]
            self.pages = [x for x in document_tree.xpath('//span[contains(@class, \'pager__pages\')]'
                                '/label/input/@value')]
        else:
            self.items = []
            self.pages = []



class SaleItem(object):

    def __init__(self, document_tree=None):
        self.is_sold = False
        self.price = ''
        self.specification_url = ''
        self.seller_comment = ''
        self.year = ''
        self.mileage = ''
        self.body = ''
        self.transmission = ''

        if not document_tree is None:
            self.parse(document_tree)


    def parse(self, document_tree):
        self.is_sold = len(document_tree.xpath('//div[contains(@class, \'card__sold-message\')]')) > 0
        self.price = get_value(document_tree, '//h4[contains(@class, \'card__price-rur\')]/text()')
        self.specification_url = get_value(document_tree, '//a[contains(@class, \'card__info-details\')]/@href')
        self.seller_comment = get_value(document_tree, '//div[contains(@class, \'seller-details__text\')]/text()')

        self.year = get_value(document_tree, u'//dt[text()= \'Год выпуска\']/following::text()')
        self.mileage = get_value(document_tree, u'//dt[text()= \'Пробег\']/following::text()')
        self.body = get_value(document_tree, u'//dt[text()= \'Кузов\']/following::text()')
        self.transmission = get_value(document_tree, u'//dt[text()= \'Коробка\']/following::text()')
        self.color = get_value(document_tree, u'//dt[text()= \'Цвет\']/following::text()')
        self.drive= get_value(document_tree, u'//dt[text()= \'Привод\']/following::text()')
        self.engine_volume = get_value(document_tree, u'//dt[text()= \'Двигатель\']/following-sibling::dd/span[1]/text()')
        self.engine_hp = get_value(document_tree, u'//dt[text()= \'Двигатель\']/following-sibling::dd/span[2]/text()')
        self.engine_type = get_value(document_tree, u'//dt[text()= \'Двигатель\']/following-sibling::dd/span[3]/text()')
        self.steering = get_value(document_tree, u'//dt[text()= \'Руль\']/following::text()')
        self.condition = get_value(document_tree, u'//dt[text()= \'Состояние\']/following::text()')
        self.owners = get_value(document_tree, u'//dt[text()= \'Владельцы\']/following::text()')
        self.certificate = get_value(document_tree, u'//dt[text()= \'ПТС\']/following::text()')
        self.tenure = get_value(document_tree, u'//dt[text()= \'Владение\']/following::text()')
        self.customs = get_value(document_tree, u'//dt[text()= \'Таможня\']/following::text()')
        self.exchange = get_value(document_tree, u'//dt[text()= \'Обмен\']/following::text()')
        self.vin = get_value(document_tree, u'//dt[text()= \'VIN\']/following::text()')
        self.autocode = get_value(document_tree, u'//dt[text()= \'Автокод\']/following::text()')

        self.location = get_value(document_tree, u'//div[contains(@class, \'sale-location\')]/text()')
        self.seller = ' '.join(
            document_tree.xpath(u'//dt[text() = \'Продавец\']/following-sibling::dd[1]//text()')
        )

    







if __name__ == '__main__':

    # test = Test()
    # print test.i, test.j
    #f = codecs.open(filename='test_item.html', encoding='utf-8')
    f = open('test_item.html')
    #f = open('test.html')

    parser = HTMLParser(encoding='utf-8')
    tree = etree.parse(f, parser)

    item = SaleItem(tree)
    print item.year, item.body, item.transmission
    #search_list = SearchList(tree)
    #print search_list.items[0].price
