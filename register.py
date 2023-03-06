import unittest
import requests


class TestOrangeHRMWebsite(unittest.TestCase):

    def setUp(self):
        self.url = 'https://www.orangehrm.com/'

    def test_home_page_load(self):
        r = requests.get(self.url)
        self.assertEqual(r.status_code, 200)

    def test_contact_sales_page_load(self):
        r = requests.get(self.url + 'contact-sales')
        self.assertEqual(r.status_code, 200)

    def test_current_vacancies_page_load(self):
        r = requests.get(self.url + 'company/careers/current-vacancies')
        self.assertEqual(r.status_code, 200)

    def test_page_download_books(self):
        r = requests.get(self.url + 'e-books')
        self.assertEqual(r.status_code, 200)

    def test_page_dictionary(self):
        r = requests.get(self.url + 'hr-dictionary')
        self.assertEqual(r.status_code, 200)
