import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from project_ChitaiGorod_ui import MainPageChitaiGorod

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture
def search_page(driver):
    page = MainPageChitaiGorod(driver)
    page.open()
    page.search_bar()
    return page

@pytest.mark.parametrize("book_list, expected_results", [
    ("Преступление и наказание", "Преступление и наказание"),
    ("ПРЕСТУПЛЕНЕ И НАКАЗАНИЕ", "Преступление и наказание"),
    ("преступление и наказание", "Преступление и наказание"),
    ("Преступление и ", "Преступление и наказание"),
    ("Professional english", "Professional english")
])
def test_book_search(search_page, book_list, expected_results):
    results = search_page.name_search(book_list)
    for book_name, expected_titles in zip(book_list, expected_results):
        assert any(expected_title in results[book_name] for expected_title in
                   expected_titles), f"Expected one of {expected_titles} in {results[book_name]} for {book_name}"

@pytest.mark.parametrize("author_list, expected_results", [
    ("Громыко", "Ольга Громыко"),
    ("Громыко Ольга Николаевна", "Ольга Громыко"),
    ("ГРОМЫКО ОЛЬГА", "Ольга Громыко"),
    ("Charles Darwin", "Charles Darwin")
])
def test_author_search(search_page, author_list, expected_results):
    results = search_page.author_search(author_list)
    for author_name, expected_authors in zip(author_list, expected_results):
        assert any(expected_author in results[author_name] for expected_author in expected_authors), \
            f"Expected one of {expected_authors} in {results[author_name]} for {author_name}"

@pytest.mark.parametrize("search_input", ["##########", "@@@@@", "123456", ";:?*()..,,"])
def test_search_not_found(search_page, search_input):
    result = search_page.search_not_found(search_input)
    assert result == 'Похоже, у нас такого нет'