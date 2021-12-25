import unittest
from city_functions import get_formatted_city_country

class CityCountryTestCase(unittest.TestCase):
	def test_city_country_test(self):
		formatted_city_country = get_formatted_city_country('Bogor', 'Indonesia')
		self.assertEqual(formatted_city_country, 'Bogor, Indonesia.')

	def test_city_country_population_test(self):
		formatted_city_country = get_formatted_city_country('Bogor', 'Indonesia', 5000)
		self.assertEqual(formatted_city_country, 'Bogor, Indonesia - population 5000')

if __name__ == '__main__':
	unittest.main()