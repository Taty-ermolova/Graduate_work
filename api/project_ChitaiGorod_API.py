import requests

class ProjectChitaiGorodApi:

    def __init__(self, url) -> None:
        self.url = url
        self.token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyNTEwOTE3LCJpYXQiOjE3NjEwMzQ3MTgsImV4cCI6MTc2MTAzODMxOCwidHlwZSI6MjAsImp0aSI6IjAxOWEwNWQ5LTRiNDMtNzg4Zi05NzRmLTRlMGNhMjhhYTM4NCIsInJvbGVzIjoxMH0.RdBwYJcLI5MqRyL1lWzwukH8YSldMBU8YyEEro6eCKQ'


    def get_list_stores(self):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url, headers=headers)
        return resp


    def get_search_book_title(self):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url, headers=headers)
        return resp

    def get_search_author_name(self):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url, headers=headers)
        return resp

    def get_list_stores_not_authorization(self):
        resp = requests.get(self.url)
        return resp

    def get_search_book_title_bad_url(self):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.get(self.url, headers=headers)
        return resp

    def get_search_author_name_incorrect_method(self):
        key = self.token
        headers = {
            'Authorization': f'Bearer {key}'
        }
        resp = requests.post(self.url, headers=headers)
        return resp
