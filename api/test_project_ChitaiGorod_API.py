from .project_ChitaiGorod_API import ProjectChitaiGorodApi

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyNTEwOTE3LCJpYXQiOjE3NjEzMTcyNzksImV4cCI6MTc2MTMyMDg3OSwidHlwZSI6MjAsImp0aSI6IjAxOWExNmIwLWQ4OGEtN2IzNC1iYTY4LTY1MTQzODk1NWYwZCIsInJvbGVzIjoxMH0.-_qXppH2ZUqG_LoNS8xl05u51oFhes6CkUyN_P6WQLc'
url='https://web-agr.chitai-gorod.ru/web/api/v2'


def test_get_list_stores():
    list_stores = ProjectChitaiGorodApi(token=token,url=url)

    response_get_list_stores = list_stores.get_list_stores(cityId=213, phrase='Ведьмак')
    assert response_get_list_stores.status_code == 200

def test_get_search_book_title():
    search_book_title = ProjectChitaiGorodApi(token=token,url=url)

    response_get_search_book_title = search_book_title.get_search_book_title(phrase='Мастер и Маргарита', perPage=48)
    assert response_get_search_book_title.status_code == 200

def test_get_search_author_name():
    search_author_name = ProjectChitaiGorodApi(token=token,url=url)

    response_get_search_author_name = search_author_name.get_search_author_name(phrase='Ольга Громыко', perPage=48)
    assert response_get_search_author_name.status_code == 200

def test_get_list_stores_not_authorization():
    list_stores_not_authorization = ProjectChitaiGorodApi(token=token,url=url)

    response_get_list_stores_not_authorization = list_stores_not_authorization.get_list_stores_not_authorization(phrase='Python', cityId=213)
    assert response_get_list_stores_not_authorization.status_code == 401
    assert response_get_list_stores_not_authorization.message == "Authorization обязательное поле"

def test_get_search_book_title_bad_url():
    search_book_title_bad_url = ProjectChitaiGorodApi(token=token,url=url)

    response_get_search_book_title_bad_url = search_book_title_bad_url.get_search_book_title_bad_url(phrase='Программирование для детей', perPage=48)
    assert response_get_search_book_title_bad_url.status_code == 404
    assert response_get_search_book_title_bad_url.message == "404 page not found"

def test_get_search_author_name_incorrect_method():
    search_author_name_incorrect_method = ProjectChitaiGorodApi(token=token,url=url)

    response_get_search_author_name_incorrect_method = search_author_name_incorrect_method.get_search_author_name_incorrect_method(phrase='Андрей Уланов', perPage=48)
    assert response_get_search_author_name_incorrect_method.status_code == 405
    assert response_get_search_author_name_incorrect_method.message == "405 method not allowed"