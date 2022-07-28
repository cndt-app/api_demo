from datetime import date
from typing import Any, Optional
from urllib.parse import urljoin

import requests

CONDUIT_API_URL = 'https://link.getconduit.app'
CONDUIT_CUSTOMER_API_KEY = ' place your api key here '

__all__ = (
    'get_credentials',
    'get_data_chunks',
)


def get_credentials() -> list[dict[str, Any]]:
    """
    Gets a list of available data drivers and theirs connected accounts.
    :return: list of drivers
    """
    res = _request('credentials/')
    return res


def get_data_chunks(
    driver_id: str,
    date_from: date,
    date_to: date,
    account_id: Optional[int] = None,
) -> dict[str, list[dict[str, str]]]:
    """
    Gets a list of data chunks for the given driver, account and date range.
    :param driver_id: driver unique slug
    :param date_from: starting date
    :param date_to: ending date
    :param account_id: if set returns data urls for this account only
    :return: lists of data chunks grouped by theirs data schema slug
    """
    params: dict[str, Any] = {
        'driver_id': driver_id,
        'date_from': date_from.isoformat(),
        'date_to': date_to.isoformat(),
    }
    if account_id:
        params['account_id'] = account_id

    res = _request('data_lake/', params)
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
