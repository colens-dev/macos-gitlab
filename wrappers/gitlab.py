import requests

class GitLabException(Exception):
        pass

class GitLabWrapper:

    def __init__(self, url='https://www.gitlab.com'):
        self.url = url

    def get_opened_merge_requests(self, username, token):
        if not username or not token:
            raise GitLabException

        headersAuth = {'Authorization': 'Bearer ' + token}
        query = {
            'reviewer_username':username,
            'view': 'simple',
            'scope': 'all',
            'state':'opened',
        }
        
        try:
            response = requests.get(f'{self.url}/api/v4/merge_requests', params=query, headers=headersAuth, verify=False)
        except requests.exceptions.RequestException as e:
            raise GitLabException

        if not response.ok:
            raise GitLabException
        return response.json()


    def get_my_merge_requests(self, username, token):
        if not username or not token:
            raise GitLabException

        headersAuth = {'Authorization': 'Bearer ' + token}
        query = {
            'author_username': username,
            'view': 'simple',
            'scope': 'all',
            'state':'opened',
        }
        
        try:
            response = requests.get(f'{self.url}/api/v4/merge_requests', params=query, headers=headersAuth, verify=False)
        except requests.exceptions.RequestException as e:
            raise GitLabException

        if not response.ok:
            raise GitLabException    
        return response.json()
