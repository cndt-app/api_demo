from datetime import datetime
from typing import Any

from conduit_companies import create_company, get_companies


def print_company_info(company: dict[str, Any]) -> None:
    print(f"Company '{company['id']}': created at: {company['created_at']}")
    token_expires_at = datetime.fromtimestamp(company['api_token']['expires_at']).isoformat()
    print(f"  Company token: {company['api_token']['token']} (expires at {token_expires_at})")

    for integration in company['connections']:
        print(f"  Integration: {integration['name']}")

        for credentials in integration['credentials']:
            print(
                "    "
                + f"Credentials: {credentials['id']}: {credentials['name']}, "
                + f"created at: {credentials['created_at']}"
            )

            for account in credentials['accounts']:
                print(f"      Account: {account['id']}: {account['name']}, native id: {account['native_id']}")


def main() -> None:
    companies = get_companies()
    if not companies:
        create_company('company1')
        companies = get_companies()

    for company in companies:
        print_company_info(company)


if __name__ == '__main__':
    main()
