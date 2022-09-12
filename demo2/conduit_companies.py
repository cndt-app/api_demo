from typing import Any
from urllib.parse import urljoin

import requests

CONDUIT_API_URL = 'https://api.getconduit.app'
CONDUIT_API_KEY = ' place your api key here '


def get_companies() -> list[dict[str, Any]]:
    """
    Returns list of companies
    :return: list of users
    """
    res = _request('link/company/?include_connections=true', method='GET')
    return res.json()


def create_company(
        company_id: str,
        name: str = None,
        page_enabled: bool = True,
) -> dict[str, Any]:
    """
    Creates a new company with given name and email.
    :param company_id: company guid(unique within API consumer)
    :param name: name of the company
    :param page_enabled: Enabling company credentials page
    """
    res = _request('link/company/', params=_get_company_params(company_id, name, page_enabled))
    return res.json()


def get_user_token(user_guid: str) -> str:
    """
    Returns user's access token.
    :param user_guid: user's guid
    :return: token
    """
    res = _request('link/auth/token/', params={'guid': user_guid})
    return res.json()['token']


def _get_company_params(company_id: str, name: str, page_enabled: bool) -> dict[str, str]:
    params = {
        'id': company_id,
    }
    if name is not None:
        params['name'] = name
    if page_enabled is not None:
        params['page_enabled'] = page_enabled

    return params


def _request(path: str, method: str = 'POST', params: dict[str, Any] = None) -> Any:
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {CONDUIT_API_KEY}',
    }
    res = requests.request(method, urljoin(CONDUIT_API_URL, path), headers=headers, json=params)
    res.raise_for_status()

    return res
