import pytest
import allure
from .config import token, url
from .project_ChitaiGorod_API import ProjectChitaiGorodApi

@pytest.mark.api
@allure.title("Тестирование получения списка магазинов")
@allure.description("Этот тест проверяет, возвращает ли API список магазинов по названию книги для данного города .")
@allure.feature("Получение данных о магазинах")
@allure.severity(allure.severity_level.NORMAL)
def test_get_list_stores():
    with allure.step("Создание экземпляра API"):
        list_stores = ProjectChitaiGorodApi(token=token, url=url)

    with allure.step("Выполнение запроса к API для получения списка магазинов"):
        response_get_list_stores = list_stores.get_list_stores(cityId=213, phrase='Ведьмак')

    with allure.step("Проверить код статуса ответа"):
        assert response_get_list_stores.status_code == 200

    with allure.step("Проверьте структуру ответа"):
        response_data = response_get_list_stores.json()
        assert isinstance(response_data, dict)
        assert 'data' in response_data
        assert isinstance(response_data['data'], list)

@pytest.mark.api
@allure.title("Поиск книги по названию")
@allure.description("Этот тест проверяет функциональность поиска по названию книги.")
@allure.feature("Поиск книг")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_search_book_title():
    with allure.step("Создание экземпляра API"):
        search_book_title = ProjectChitaiGorodApi(token=token, url=url)

    with allure.step("Отправить запрос на поиск книги по названию"):
        response_get_search_book_title = search_book_title.get_search_book_title(phrase='Мастер и Маргарита', perPage=48)

    with allure.step("Проверить код статуса ответа"):
        assert response_get_search_book_title.status_code == 200

    with allure.step("Проверка структуры данных ответа"):
        response_data = response_get_search_book_title.json()
        assert 'data' in response_data
        assert 'products' in response_data['data']
        assert isinstance(response_data['data']['products'], list)

    with allure.step("Проверить, есть ли книга в списке товаров"):
        found = any(product['title'] == "Мастер и Маргарита" for product in response_data['data']['products'])
        assert found, "Книга 'Мастер и Маргарита' не найдена в списке продуктов"

    with allure.step("Убедиться, что цены на продукцию неотрицательны."):
        for product in response_data['data']['products']:
            assert product['price'] >= 0, f"Цена книги {product['title']} отрицательная"

    with allure.step("Проверить количество продуктов"):
        assert len(response_data['data']['products']) <= 48, "Количество продуктов превышает ожидаемое"


@pytest.mark.api
@allure.title("Тестовый поиск по имени автора")
@allure.description("Этот тест ищет книги по имени автора 'Ольга Громыко'")
@allure.feature("Поиск авторов")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_search_author_name():
    with allure.step("Создание экземпляра API"):
        search_author_name = ProjectChitaiGorodApi(token=token, url=url)

    with allure.step("Выполнение запроса к API для поиска автора"):
        response_get_search_author_name = search_author_name.get_search_author_name(phrase='Ольга Громыко', perPage=48)

    with allure.step("Проверить код статуса ответа"):
        assert response_get_search_author_name.status_code == 200

    with allure.step("Проверка структуры данных ответа"):
        response_data = response_get_search_author_name.json()
        assert 'data' in response_data
        assert 'products' in response_data['data']
        assert isinstance(response_data['data']['products'], list)

    with allure.step("Подтвердить список продуктов"):
        products = response_data['data']['products']
        assert len(products) > 0

    with allure.step("Проверить, найден ли автор"):
        author_found = any(
            product['authors'][0]['firstName'] == 'Ольга' and
            product['authors'][0]['lastName'] == 'Громыко'
            for product in products
        )
        assert author_found

    with allure.step("Проверка ключей продукта"):
        for product in products:
            assert 'id' in product
            assert 'price' in product
            assert 'title' in product

@pytest.mark.api
@allure.title("Тест на получение списка магазинов без авторизации")
@allure.description("Проверка получения списка магазинов без авторизации, ожидание ошибки 401")
@allure.feature("Получение данных о магазинах")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_list_stores_not_authorization():
    with allure.step("Создание экземпляра API без авторизации"):
        list_stores_not_authorization = ProjectChitaiGorodApi(token=token,url=url)

    with allure.step("Выполнение запроса к API для получения списка магазинов"):
        response_get_list_stores_not_authorization = list_stores_not_authorization.get_list_stores_not_authorization(phrase='Python', cityId=213)

    with allure.step("Проверить код статуса ответа"):
        assert response_get_list_stores_not_authorization.status_code == 401

    with allure.step("Проверка сообщения об ошибке в ответе"):
        response_json = response_get_list_stores_not_authorization.json()
        assert response_json["message"] == "Authorization обязательное поле"

@pytest.mark.api
@allure.title("Тест на поиск книги по неправильному URL")
@allure.description("Проверка поиска книги по неправильному URL, ожидание ошибки 404")
@allure.feature("Поиск книг")
@allure.severity(allure.severity_level.NORMAL)
def test_get_search_book_title_bad_url():
    with allure.step("Создание экземпляра API для поиска по неправильному URL"):
        search_book_title_bad_url = ProjectChitaiGorodApi(token=token,url=url)

    with allure.step("Выполнение запроса к API для поиска книги по неправильному URL"):
        response_get_search_book_title_bad_url = search_book_title_bad_url.get_search_book_title_bad_url(phrase='Программирование для детей', perPage=48)

    with allure.step("Проверить код статуса ответа и сообщения об ошибке в ответе"):
        assert response_get_search_book_title_bad_url.status_code == 404
        assert "404 page not found" in response_get_search_book_title_bad_url.text

@pytest.mark.api
@allure.title("Тест на поиск автора с неправильным методом запроса")
@allure.description("Проверка поиска автора с использованием неправильного метода запроса, ожидание ошибки 405")
@allure.feature("Поиск авторов")
@allure.severity(allure.severity_level.MINOR)
def test_get_search_author_name_incorrect_method():
    with allure.step("Создание экземпляра API для поиска автора с неправильным методом"):
        search_author_name_incorrect_method = ProjectChitaiGorodApi(token=token,url=url)

    with allure.step("Выполнение запроса к API для поиска автора с неправильным методом запроса"):
        response_get_search_author_name_incorrect_method = search_author_name_incorrect_method.get_search_author_name_incorrect_method(phrase='Андрей Уланов', perPage=48)

    with allure.step("Проверить код статуса ответа и сообщения об ошибке в ответе"):
        assert response_get_search_author_name_incorrect_method.status_code == 405
        assert "405 method not allowed" in response_get_search_author_name_incorrect_method.text