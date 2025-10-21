from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class MainPageChitaiGorod:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)
        self.driver.maximize_window()

    def open(self):
        self.driver.get(
            "https://www.chitai-gorod.ru/"
        )

    def search_bar(self):
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "input.search-form__input.search-form__input--search")))
        self.search_bar = self.driver.find_element(By.CSS_SELECTOR, "input.search-form__input.search-form__input--search")
        self.search_bar.click()

    def name_search(self, book_list):
        results = {}
        for book_name in book_list:
            self.search_bar.clear()
            self.search_bar.send_keys(book_name)
            self.search_bar.send_keys(Keys.ENTER)
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.product-card__title"))
            )

            book_titles_elements = self.driver.find_elements(By.CSS_SELECTOR, "a.product-card__title")
            titles = [title_element.text for title_element in book_titles_elements]
            results[book_name] = titles
        return results

    def author_search(self, author_list):
        results = {}
        for author_name in author_list:
            self.search_bar.clear()
            self.search_bar.send_keys(author_name)
            self.search_bar.send_keys(Keys.ENTER)
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.product-card__subtitle"))
            )

            book_author_elements = self.driver.find_elements(By.CSS_SELECTOR, "span.product-card__subtitle")
            authors = [author_element.text for author_element in book_author_elements]
            results[author_name] = authors
        return results

    def search_not_found(self,search_input):
        self.search_bar.send_keys(search_input)
        self.search_bar.send_keys(Keys.ENTER)
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h4.catalog-stub__title"))
        )

        not_found = self.driver.find_element(By.CSS_SELECTOR, "h4.catalog-stub__title")
        return not_found.text

