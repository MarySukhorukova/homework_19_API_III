import logging
from requests import Session, Response
from curlify import to_curl


def allure_logger(function):
    def wrapper(*args, **kwargs):
        response: Response = function(*args, **kwargs)
        logging.info(f'{response.status_code} {to_curl(response.request)}')

        return response

    return wrapper


class BaseSession(Session):
    def __init__(self, url):
        super(BaseSession, self).__init__()
        self.url = url

    @allure_logger
    def request(self, method, url, **kwargs) -> Response:
        response = super().request(method, self.url + url, **kwargs)
        logging.info(f'{response.status_code} {to_curl(response.request)}')
        return response