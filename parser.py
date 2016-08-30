from io import StringIO
from lxml import etree
from lxml.etree import HTMLParser


class SearchItem(object):
	
	
	def __init__(self, tree=None):
		self.model = ''
		self.price = ''
		self.mileage = ''

		if not tree is None:
			self.parse(tree)
		
	
	def _get_value(self, tree, xpath):
		result = tree.xpath(xpath)
		if result:
			return result[0].strip()
		else:
			return None


	def parse(self, tree):
		self.year = self._get_value(tree, './/div[contains(@class, \'listing-item__year\')]/text()')
		self.mileage = self._get_value(tree, './/div[contains(@class, \'listing-item__km\')]/text()')
		self.description = self._get_value(tree, './/div[contains(@class, \'listing-item__description\')]/text()')
		self.price = self._get_value(tree, './/div[contains(@class, \'listing-item__price\')]/text()')
		self.currency = self._get_value(tree, './/div[contains(@class, \'listing-item__price\')]/div[contains(@class, \'i-currency-symbol__seo-currency\')]/text()')
		self.url = self._get_value(tree, './/a[contains(@class, \'listing-item__link\')]/@href')
		self.model = self._get_value(tree, './/a[contains(@class, \'listing-item__link\')]/text()') + ' ' + self._get_value(tree, './/span[contains(@class, \'listing-item__avtokod\')]/text()')
	
class SearchList(object):
	
	def __init__(self, tree=None):
		if not tree is None:
			self.items = [SearchItem(x) for x in tree.xpath('//tbody[contains(@class, \'listing-item\') and @data-bem]')]
			self.pages = [x for x in tree.xpath('//span[contains(@class, \'pager__pages\')]/label/input/@value')]
		else:
			self.items = []
			self.pages = []

	

class SaleItem(object):
	
	def __init__(self, tree=None):
		if not tree is None:
			self.parse(tree)
		
	def parse(self, tree):
		self.properties = ItemProperties(tree)


class ItemProperties(object):
	
	def __init__(self, tree=None):
		pass

	def parse(self, tree):
		
		self.year = self._get_value(tree, './/div[contains(@class, \'listing-item__year\')]/text()')
		

if __name__ == '__main__':
	
	# test = Test()
	# print test.i, test.j
	f = open('test_item.html')
		
	parser = HTMLParser()
	tree = etree.parse(f, parser)
	
	search_list = SaleItem(tree)
	print search_list.properties
