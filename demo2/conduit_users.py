from typing import Any
from urllib.parse import urljoin

import requests

CONDUIT_API_URL = 'https://link.getconduit.app'
CONDUIT_API_KEY = ' place your api key here '


def get_users() -> str:
    """
    Returns list of consumer's users.
    :return: list of users
    """
    res = _request('users/', method='GET')
    return res.json()


def get_users_info() -> str:
    """
    Returns list of consumer's users with theirs connections and access tokens.
    :return: list of users info
    """
    res = _request('users/info/', method='GET')
    return res.json()


def create_user(user_guid: str, name: str = None, email: str = None) -> dict[str, Any]:
    """
    Creates a new user with given name and email.
    :param user_guid: user's guid (unique within API consumer)
    :param name: name of the user
    :param email: user's email (unique within the system)
    """
    res = _request('users/', params=_get_user_params(user_guid, name, email))
    return res.json()


def get_user_token(user_guid: str) -> str:
    """
    Returns user's access token.
    :param user_guid: user's guid
    :return: token
    """
    res = _request('auth/token/', params={'guid': user_guid})
    return res.json()['token']


def _get_user_params(user_guid: str, name: str = None, email: str = None) -> dict[str, str]:
    params = {
        'guid': user_guid,
    }
    if name is not None:
        params['name'] = name
    if email is not None:
        params['email'] = email

    return params


def _request(path: str, method: str = 'POST', params: dict[str, Any] = None) -> Any:
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {CONDUIT_API_KEY}',
    }
    res = requests.request(method, urljoin(CONDUIT_API_URL, path), headers=headers, json=params)
    res.raise_for_status()

    return res
