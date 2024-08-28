import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Farooq has heard about a cool new online to-do app.
        # She goes to check out its homepage.
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists.
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do list", header_text)

        # She is invited to enter a to-do item straight away.
        input_box = self.browser.find_element(By.ID, "new_todo")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Buy peacock feathers" into a text box (Edith's hobby is fly-fishing lures).
        input_box.send_keys("Buy peacock feathers")
        time.sleep(1)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list.
        table = self.browser.find_element(By.ID, "todo_list")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == "1: Buy peacock feathers" for row in rows))

        # There is still a test box inviting her to add another item.
        input_box = self.browser.find_element(By.ID, "new_todo")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")
        
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical).
        input_box.send_keys("Buy peacock feathers")
        time.sleep(1)

        # The page updates again and shows both items on her list.
        table = self.browser.find_element(By.ID, "todo_list")
        rows = table.find_elements(By.TAG_NAME, "tr")
        
        expected_items = {"1: Buy peacock feathers", "2: Use peacock feathers to make a fly"}
        self.assertTrue(any(row.text in expected_items for row in rows))
        
# Satisfied, she goes back to sleep.

if __name__ == "__main__":
    unittest.main()