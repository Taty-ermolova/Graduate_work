from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException

class MainPageChitaiGorod:
    """
    Класс для работы с основной страницей сайта "Читай-город".

    Атрибуты:
    driver : WebDriver, объект WebDriver для взаимодействия с браузером.
    wait : WebDriverWait, объект WebDriverWait для ожидания элементов на странице.
    """

    def __init__(self, driver):
        """
        Инициализирует объект.
        Параметры:
        driver: объект WebDriver, который управляет браузером.
        Возвращаемое значение: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)
        self.driver.maximize_window()

    def open(self):
        """
        Открывает главную страницу сайта "Читай-город"
        Параметры: нет
        Возвращаемое значение: None
        """
        self.driver.get(
            "https://www.chitai-gorod.ru/"
        )

    def find_search_bar(self):
        """
        Открывает главную страницу сайта "Читай-город"
        Параметры: нет
        Возвращаемое значение: None
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "input.search-form__input.search-form__input--search")))
        self.search_bar = self.driver.find_element(By.CSS_SELECTOR, "input.search-form__input.search-form__input--search")
        self.search_bar.click()

    def name_search(self, book_name):
        """
        Выполняет поиск книги по её названию, вводит название в строку поиска и собирает заголовки найденных книг.
        Параметры: book_name: строка, представляющая название книги для поиска.
        Возвращаемое значение: словарь, где ключ — это название книги, а значение — список заголовков найденных книг.
        """
        results = {}
        self.search_bar.clear()
        self.search_bar.send_keys(book_name)
        self.search_bar.send_keys(Keys.ENTER)
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.product-card__title"))
        )
        sleep(3)

        try:
            titles = self._get_titles_safely()
            results[book_name] = titles
            return results

        except Exception as e:
            print(f"Ошибка при получении заголовков: {e}")
            results[book_name] = []
            return results

    def _get_titles_safely(self):
        """
        Частный метод, безопасно получающий заголовки книг с обработкой исключения StaleElementReferenceException.
        Параметры: нет
        Возвращаемое значение: list заголовков книг, найденных на странице.
        """
        max_attempts = 3
        titles = []

        for attempt in range(max_attempts):
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, "a.product-card__title")
                print(f"Попытка {attempt + 1}: найдено {len(elements)} элементов")

                titles = []
                for i in range(len(elements)):
                    try:
                        current_elements = self.driver.find_elements(By.CSS_SELECTOR, "a.product-card__title")
                        if i < len(current_elements):
                            text = current_elements[i].text
                            if text.strip():
                                titles.append(text)
                                print(f"  Добавлен заголовок: {text}")
                    except StaleElementReferenceException:
                        print(f"  Элемент {i} устарел, пропускаем")
                        continue

                if titles:
                    return titles

            except Exception as e:
                print(f"Ошибка в попытке {attempt + 1}: {e}")

            sleep(1)

        return titles

    def author_search(self, author_name):
        """
        Выполняет поиск по имени автора, вводит имя в строку поиска и собирает авторов найденных книг.
        Параметры: author_name: str, представляющая имя автора для поиска.
        Возвращаемое значение: dict, где ключ — это имя автора, а значение — список авторов найденных книг.
        """
        results = {}
        self.search_bar.clear()
        self.search_bar.send_keys(author_name)
        self.search_bar.send_keys(Keys.ENTER)
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.product-card__subtitle"))
        )

        try:
            authors = self._get_authors_safely()
            results[author_name] = authors
            return results
        except Exception as e:
            print(f"Ошибка при получении авторов: {e}")
            results[author_name] = []
            return results


    def _get_authors_safely(self):
        """
        Частный метод, безопасно получающий имена авторов с обработкой исключения StaleElementReferenceException.
        Параметры: нет
        Возвращаемое значение: list имен авторов, найденных на странице.
        """
        max_attempts = 3
        authors = []

        for attempt in range(max_attempts):
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, "span.product-card__subtitle")
                print(f"Попытка {attempt + 1}: найдено {len(elements)} элементов")

                authors = []
                for i in range(len(elements)):
                    try:
                        current_elements = self.driver.find_elements(By.CSS_SELECTOR, "span.product-card__subtitle")
                        if i < len(current_elements):
                            text = current_elements[i].text
                            if text.strip():  # только непустые тексты
                                authors.append(text)
                                print(f"  Добавлен автор: {text}")
                    except StaleElementReferenceException:
                        print(f"  Элемент {i} устарел, пропускаем")
                        continue

                if authors:
                    return authors

            except Exception as e:
                print(f"Ошибка в попытке {attempt + 1}: {e}")

            sleep(1)

        return authors

    def search_not_found(self,search_input):
        """
        Выполняет поиск на сайте и проверяет, что товар не найден
        Параметры:
        search_input : str, строка поиска, вводимая в поисковую строку сайта.
        Возвращает: str, текст элемента, указывающего, что товар не найден.
        """
        self.search_bar.send_keys(search_input)
        self.search_bar.send_keys(Keys.ENTER)
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h4.catalog-stub__title"))
        )

        not_found = self.driver.find_element(By.CSS_SELECTOR, "h4.catalog-stub__title")
        return not_found.text