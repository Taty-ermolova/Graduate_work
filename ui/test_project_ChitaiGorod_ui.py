import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from .project_ChitaiGorod_ui import MainPageChitaiGorod

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

@pytest.mark.parametrize("book_name, expected_titles", [
    ("Преступление и наказание", "Преступление и наказание"),
    ("Professional english", "Professional english")
])
def test_book_search(search_page, book_name, expected_titles):
    results = search_page.name_search([book_name])
    found_titles = results[book_name]
    assert any(title in found_titles for title in expected_titles), f"Не найдены ожидаемые названия для {book_name}"

@pytest.mark.parametrize("author_name, expected_authors", [
    ("ГРОМЫКО ОЛЬГА", "Ольга Громыко"),
    ("Charles Darwin", "Charles Darwin")
])
def test_author_search(search_page, author_name, expected_authors):
    results = search_page.author_search([author_name])
    found_authors = results[author_name]
    assert any(author in found_authors for author in expected_authors), f"Не найдены ожидаемые авторы для {author_name}"

@pytest.mark.parametrize("search_input", ["##########", "??????????"])
def test_search_not_found(search_page, search_input):
    result = search_page.search_not_found(search_input)
    assert result == 'Похоже, у нас такого нет'
