import requests

class ProjectChitaiGorodApi:

    def __init__(self, url, token) -> None:
        self.url = url
        self.token = token


    def get_list_stores(self, cityId, phrase):
        params = {
            'customerCityId': cityId,
            'phrase': phrase
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.get(self.url+'/search/facet-search', headers=headers, params = params)
        return resp


    def get_search_book_title(self, phrase, perPage):
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
        params = {
            'phrase': phrase,
            'perPage': perPage
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.post(self.url+'v1/recommend/semantic', headers=headers, params = params)
        return resp
