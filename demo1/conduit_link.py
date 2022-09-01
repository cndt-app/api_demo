from datetime import date
from typing import Any, Optional
from urllib.parse import urljoin

import requests

CONDUIT_API_URL = 'https://api.getconduit.app'
CONDUIT_CUSTOMER_API_KEY = ' place your api key here '

__all__ = (
    'get_credentials',
    'get_data_chunks',
)


def get_credentials() -> list[dict[str, Any]]:
    """
    Gets a list of available integrations and theirs connected accounts.
    :return: list of integrations
    """
    res = _request('link/credentials/')
    return res


def get_data_chunks(
    integration: str,
    date_from: date,
    date_to: date,
    account: Optional[int] = None,
) -> dict[str, list[dict[str, str]]]:
    """
    Gets a list of data chunks for the given integration, account and date range.
    :param integration: integration unique name
    :param date_from: starting date
    :param date_to: ending date
    :param account: if set returns data urls for this account only
    :return: lists of data chunks grouped by theirs data schema
    """
    params: dict[str, Any] = {
        'integration': integration,
        'date_from': date_from.isoformat(),
        'date_to': date_to.isoformat(),
    }
    if account:
        params['account'] = account

    res = _request('link/data_lake/', params)
    return res


def _request(path: str, params: dict[str, Any] = None) -> Any:
    headers = {
        'accept': 'application/json',
    }
    params = params or {}
    params['token'] = CONDUIT_CUSTOMER_API_KEY

    res = requests.request('GET', urljoin(CONDUIT_API_URL, path), headers=headers, params=params)
    res.raise_for_status()

    return res.json()
