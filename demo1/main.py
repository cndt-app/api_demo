import os
from datetime import date, timedelta

import requests
from conduit_link import get_credentials, get_data_chunks

DATA_DIR = os.path.join(os.getcwd(), 'data')


def main(date_range: tuple[date, date]) -> None:
    # Getting a list of available drivers and theirs connected accounts
    credentials = get_credentials()

    for driver in credentials:
        print(f"Driver: {driver['name']}")

        for credentials in driver['credentials']:
            print(f"  Credentials: {credentials['id']}:{credentials['name']}, created at: {credentials['created_at']}")

            for account in credentials['accounts']:
                print(f"    Account: {account['id']}:{account['name']}, native id: {account['native_id']}")

                path = os.path.join(DATA_DIR, driver['id'], str(credentials['id']), str(account['id']))
                os.makedirs(path, exist_ok=True)

                process_data_chunks(driver['id'], account['id'], path, date_range)


def process_data_chunks(driver_id: str, account_id: int, path: str, date_range: tuple[date, date]) -> None:
    date_from, date_to = date_range

    # Getting a list of data chunks
    data_chunks = get_data_chunks(driver_id, date_from, date_to, account_id)

    for schema_slug, chunks in data_chunks.items():
        for chunk in chunks:
            print(
                "      "
                + f"{chunk['date']}: "
                + f"schema: {schema_slug} "
                + f"service_status: {chunk['service_status']}, "
                + f"data_status: {chunk['data_status']}, "
                + f"updated_at: {chunk['data_updated_at']}"
            )

            download_data_chunk(chunk['url'], os.path.join(path, f"{chunk['date']}.csv"))


def download_data_chunk(url: str, filename: str) -> None:
    try:
        res = requests.get(url)
        res.raise_for_status()

        with open(filename, 'wb') as f:
            f.write(res.content)

    except requests.exceptions.RequestException as ex:
        print(ex)


if __name__ == '__main__':
    date_range = (date.today() - timedelta(days=6), date.today())
    main(date_range)
