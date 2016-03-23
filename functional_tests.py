from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retive_it_later(self):
        self.browser.get('http://localhost:8000')

        assert 'Django' in self.browser.title, "Browser title was {}".format(self.browser.title)



if __name__ == '__main__':
    unittest.main(warnings='ignore')
