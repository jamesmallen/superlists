from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from superlists import settings
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it(self):
        # Sally opens the homepage
        self.browser.get('http://localhost:8000')

        # Sally looks for the title of the homepage
        self.assertIn(
            settings.SITE_NAME, self.browser.title,
            'Browser title was {}'.format(self.browser.title)
        )

        # Sally looks for the title again
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(
            settings.SITE_NAME, header_text
        )

        # Sally looks for the box to type new todo items
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Sally types a todo item
        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)

        # Sally looks to see that the item is now in her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # Sally creates a new todo item using hte peacock feathers


if __name__ == '__main__':
    unittest.main()
