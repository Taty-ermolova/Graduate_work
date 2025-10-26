import requests

class ProjectChitaiGorodApi:
    """
    Класс для взаимодействия с API "Читай-город".

    Атрибуты:
    url (str): Базовый URL API.
    token (str): Токен для авторизации.
    """

    def __init__(self, url, token) -> None:
        """
        Инициализирует объект с URL и токеном.
        Параметры:
        url (str): Базовый URL API.
        token (str): Токен для авторизации.
        Возвращаемое значение: None
        """
        self.url = url
        self.token = token


    def get_list_stores(self, cityId, phrase):
        """
        Получает список магазинов по ID города и фразе.
        Параметры:
        cityId (int): Идентификатор города.
        phrase (str): Поисковая фраза.

        Возвращаемое значение:
        Response: Объект ответа от requests.get.
        """
        params = {
            'customerCityId': cityId,
            'phrase': phrase
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.get(self.url+'v2/search/facet-search', headers=headers, params = params)
        return resp


    def get_search_book_title(self, phrase, perPage):
        """
        Ищет книги по названию.
        Параметры:
        phrase (str): Поисковая фраза.
        perPage (int): Количество результатов на страницу.

        Возвращаемое значение:
        Response: Объект ответа от requests.get.
        """
        params = {
            'phrase': phrase,
            'perPage': perPage
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.get(self.url+'v1/recommend/semantic', headers=headers, params = params)
        return resp

    def get_search_author_name(self, phrase, perPage):
        """
        Ищет книги по имени автора.
        Параметры:
        phrase (str): Поисковая фраза.
        perPage (int): Количество результатов на страницу.

        Возвращаемое значение:
        Response: Объект ответа от requests.get.
        """
        params = {
            'phrase': phrase,
            'perPage': perPage
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.get(self.url+'v1/recommend/semantic', headers=headers, params = params)
        return resp

    def get_list_stores_not_authorization(self, cityId, phrase):
        """
        Получает список магазинов по ID города и фразе без использования авторизации
        Параметры:
        Параметры:
        cityId (int): Идентификатор города.
        phrase (str): Поисковая фраза.

        Возвращаемое значение:
        Response: Объект ответа от requests.get.
        """
        params = {
            'cityId': cityId,
            'phrase': phrase
        }
        headers = {
            'Authorization': ''
        }
        resp = requests.get(self.url+'v2/search/facet-search',headers=headers, params = params)
        return resp

    def get_search_book_title_bad_url(self, phrase, perPage):
        """
        Ищет книги по названию, но использует неправильный URL.
        Параметры:
        phrase (str): Поисковая фраза.
        perPage (int): Количество результатов на страницу.

        Возвращаемое значение:
        Response: Объект ответа от requests.get.
        """
        params = {
            'phrase': phrase,
            'perPage': perPage
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.get(self.url, headers=headers, params = params)
        return resp

    def get_search_author_name_incorrect_method(self, phrase, perPage):
        """
        Ищет книги по имени автора, но использует неправильный HTTP-метод (POST вместо GET).
        Параметры:
        phrase (str): Поисковая фраза.
        perPage (int): Количество результатов на страницу.

        Возвращаемое значение:
        Response: Объект ответа от requests.get.
        """
        params = {
            'phrase': phrase,
            'perPage': perPage
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.post(self.url+'v1/recommend/semantic', headers=headers, params = params)
        return resp
