import requests


class GitLabException(Exception):
    pass


class GitLabSession(requests.Session):

    AUTH_DOMAINS = ['gitlab.com']

    def rebuild_auth(self, prepared_request, response):
        # Keep headers upon redirect as long as we are
        # on any of self.AUTH_DOMAINS
        headers = prepared_request.headers
        url = prepared_request.url
        if 'Authorization' in headers:
            original_parsed = requests.utils.urlparse(response.request.url)
            redirect_parsed = requests.utils.urlparse(url)
            original_domain = '.'.join(
                original_parsed.hostname.split('.')[-2:]
            )
            redirect_domain = '.'.join(
                redirect_parsed.hostname.split('.')[-2:]
            )
            if (
                    original_domain != redirect_domain and
                    redirect_domain not in self.AUTH_DOMAINS and
                    original_domain not in self.AUTH_DOMAINS):
                del headers['Authorization']


class GitLabWrapper:

    def __init__(self, url='https://www.gitlab.com'):
        self.url = url
        self.session = GitLabSession()

    def get_opened_merge_requests(self, username, token):
        if not username or not token:
            raise GitLabException

        headersAuth = {'Authorization': 'Bearer ' + token}
        query = {
            'reviewer_username': username,
            'view': 'simple',
            'scope': 'all',
            'state': 'opened',
        }

        try:
            response = self.session.get(
                f'{self.url}/api/v4/merge_requests',
                params=query,
                headers=headersAuth,
                verify=False
            )
        except requests.exceptions.RequestException:
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
            'state': 'opened',
        }

        try:
            response = self.session.get(
                f'{self.url}/api/v4/merge_requests',
                params=query,
                headers=headersAuth,
                verify=False
            )
        except requests.exceptions.RequestException:
            raise GitLabException

        if not response.ok:
            raise GitLabException
        return response.json()
