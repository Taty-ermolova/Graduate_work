from project_ChitaiGorod_API import ProjectChitaiGorodApi

def test_get_list_stores():
    list_stores = ProjectChitaiGorodApi(url='https://web-gate.chitai-gorod.ru/api/v2/search/facet-search?customerCityId=213&phrase=%D0%9F%D1%80%D0%B5%D1%81%D1%82%D1%83%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%BD%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5')

    response_get_list_stores = list_stores.get_list_stores()
    assert response_get_list_stores.status_code == 200

def test_get_search_book_title():
    search_book_title = ProjectChitaiGorodApi(url='https://web-gate.chitai-gorod.ru/api/v1/recommend/semantic?phrase=%D0%BF%D1%80%D0%B5%D1%81%D1%82%D1%83%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5+%D0%B8+%D0%BD%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5&perPage=48')

    response_get_search_book_title = search_book_title.get_search_book_title()
    assert response_get_search_book_title.status_code == 200

def test_get_search_author_name():
    search_author_name = ProjectChitaiGorodApi(url='https://web-gate.chitai-gorod.ru/api/v1/recommend/semantic?phrase=%D0%B3%D1%80%D0%BE%D0%BC%D1%8B%D0%BA%D0%BE+%D0%BE%D0%BB%D1%8C%D0%B3%D0%B0&perPage=48')

    response_get_search_author_name = search_author_name.get_search_author_name()
    assert response_get_search_author_name.status_code == 200

def test_get_list_stores_not_authorization():
    list_stores_not_authorization = ProjectChitaiGorodApi(url='https://web-gate.chitai-gorod.ru/api/v2/search/facet-search?customerCityId=213&phrase=%D0%9F%D1%80%D0%B5%D1%81%D1%82%D1%83%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%BD%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5')

    response_get_list_stores_not_authorization = list_stores_not_authorization.get_list_stores_not_authorization()
    assert response_get_list_stores_not_authorization.status_code == 401
    assert response_get_list_stores_not_authorization.message == "Authorization обязательное поле"

def test_get_search_book_title_bad_url():
    search_book_title_bad_url = ProjectChitaiGorodApi(url='https://web-gate.chitai-gorod.ru/api')

    response_get_search_book_title_bad_url = search_book_title_bad_url.get_search_book_title_bad_url()
    assert response_get_search_book_title_bad_url.status_code == 404
    assert response_get_search_book_title_bad_url.message == "404 page not found"

def test_get_search_author_name_incorrect_method():
    search_author_name_incorrect_method = ProjectChitaiGorodApi(url='https://web-gate.chitai-gorod.ru/api/v1/recommend/semantic?phrase=%D0%B3%D1%80%D0%BE%D0%BC%D1%8B%D0%BA%D0%BE+%D0%BE%D0%BB%D1%8C%D0%B3%D0%B0&perPage=48')

    response_get_search_author_name_incorrect_method = search_author_name_incorrect_method.get_search_author_name_incorrect_method()
    assert response_get_search_author_name_incorrect_method.status_code == 405
    assert response_get_search_author_name_incorrect_method.message == "405 method not allowed"