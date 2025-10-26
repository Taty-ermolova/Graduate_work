import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from .project_ChitaiGorod_ui import MainPageChitaiGorod
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture
def search_page(driver):
    page = MainPageChitaiGorod(driver)
    page.open()
    page.find_search_bar()
    return page

@pytest.mark.ui
@pytest.mark.parametrize("book_name, expected_titles", [
    ("Преступление и наказание", "Преступление и наказание"),
    ("Professional english", "Professional english")
])
@allure.title("Тест поиска книги")
@allure.description("Поиск книги по названию и проверка результатов")
@allure.feature("Поиск книг")
@allure.severity(allure.severity_level.NORMAL)
def test_book_search(search_page, book_name, expected_titles):
    with allure.step(f"Выполняется поиск книги: {book_name}"):
        results = search_page.name_search(book_name)
    found_titles = results[book_name]
    with allure.step("Проверка найденных названий"):
        assert any(expected_titles in title for title
                   in found_titles), f"Не найдены ожидаемые названия для {book_name}. Найдены: {found_titles}"


@pytest.mark.ui
@pytest.mark.parametrize("author_name, expected_authors", [
    ("ГРОМЫКО ОЛЬГА", "Ольга Громыко"),
    ("Charles Darwin", "Charles Darwin")
])
@allure.title("Тест поиска автора")
@allure.description("Поиск книги по имени автора и проверка результатов")
@allure.feature("Поиск книг по имени автора")
@allure.severity(allure.severity_level.NORMAL)
def test_author_search(search_page, author_name, expected_authors):
    with allure.step(f"Выполняется поиск автора: {author_name}"):
        results = search_page.author_search(author_name)
    found_authors = results[author_name]
    with allure.step("Проверка найденных имен авторов"):
        assert any(expected_authors in author for author in
               found_authors), f"Не найдены ожидаемые авторы для {author_name}. Найдены: {found_authors}"


@pytest.mark.ui
@pytest.mark.parametrize("search_input", ["##########", "??????????", "192837465"])
@allure.title("Тест поиска: негативные проверки")
@allure.description("Тестирование функции поиска с использованием негативных запросов и проверка результатов")
@allure.feature("Тестирование функции поиска при негативных запросах")
@allure.severity(allure.severity_level.NORMAL)
def test_search_not_found(search_page, search_input):
    with allure.step(f"Выполняется поиск по запросу: {search_input}"):
        result = search_page.search_not_found(search_input)
    with allure.step("Проверка наличия сообщения об ошибке"):
        assert result == 'Похоже, у нас такого нет'
