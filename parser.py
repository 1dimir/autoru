# -*- coding: utf-8 -*-

import codecs
from lxml import etree
from lxml.etree import HTMLParser



def get_value(tree, xpath):
	result = tree.xpath(xpath)
	if result:
		return result[0].strip()
	else:
		return None
	

class SearchItem(object):
	
	
	def __init__(self, tree=None):
		self.model = ''
		self.price = ''
		self.mileage = ''

		if not tree is None:
			self.parse(tree)
		
	
	def parse(self, tree):
		self.year = get_value(tree, './/div[contains(@class, \'listing-item__year\')]/text()')
		self.mileage = get_value(tree, './/div[contains(@class, \'listing-item__km\')]/text()')
		self.description = get_value(tree, './/div[contains(@class, \'listing-item__description\')]/text()')
		self.price = get_value(tree, './/div[contains(@class, \'listing-item__price\')]/text()')
		self.currency = get_value(tree, './/div[contains(@class, \'listing-item__price\')]'
			'/div[contains(@class, \'i-currency-symbol__seo-currency\')]/text()')
		self.url = get_value(tree, './/a[contains(@class, \'listing-item__link\')]/@href')
		self.model = get_value(tree, './/a[contains(@class, \'listing-item__link\')]/text()') + \
			' ' + \
			get_value(tree, './/span[contains(@class, \'listing-item__avtokod\')]/text()')
	
class SearchList(object):
	
	def __init__(self, tree=None):
		if not tree is None:
			self.items = [
				SearchItem(x) for x in tree.xpath('//tbody[contains(@class, \'listing-item\')'
								 'and @data-bem]')
			]
			self.pages = [x for x in tree.xpath('//span[contains(@class, \'pager__pages\')]'
								'/label/input/@value')]
		else:
			self.items = []
			self.pages = []

	

class SaleItem(object):
	
	def __init__(self, tree=None):
		if not tree is None:
			self.parse(tree)
		
	def parse(self, tree):
		self.is_sold = len(tree.xpath('//div[contains(@class, \'card__sold-message\')]')) > 0
		self.price = get_value(tree, '//h4[contains(@class, \'card__price-rur\')]/text()')
		self.specification_url = get_value(tree, '//a[contains(@class, \'card__info-details\')]/@href')
		self.seller_comment = get_value(tree, '//div[contains(@class, \'seller-details__text\')]/text()')
		
		self.year = get_value(tree, u'//dt[text()= \'Год выпуска\']/following::text()')
		self.mileage = get_value(tree, u'//dt[text()= \'Пробег\']/following::text()')
		self.body = get_value(tree, u'//dt[text()= \'Кузов\']/following::text()')
		self.transmission = get_value(tree, u'//dt[text()= \'Коробка\']/following::text()')



if __name__ == '__main__':
	
	# test = Test()
	# print test.i, test.j
	f = codecs.open(filename='test_item.html', encoding='utf-8')
	#f = open('test.html')
		
	parser = HTMLParser(encoding='utf-8')
	tree = etree.parse(f, parser)
	
	item = SaleItem(tree)
	print item.year, item.body, item.transmission
	#search_list = SearchList(tree)
	#print search_list.items[0].price
