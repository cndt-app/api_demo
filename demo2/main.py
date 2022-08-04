from typing import Any
from datetime import datetime

from conduit_users import create_user, get_users_info


def print_user_info(user: dict[str, Any]) -> None:
    print(f"User '{user['guid']}': created at: {user['created_at']}")
    print(f"  User's token: {user['token']['token']}")
    print(f"  User's token expires at: {datetime.fromtimestamp(user['token']['expires_at'])}")

    for integration in user['connections']:
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
    users_info = get_users_info()

    if not users_info:
        create_user('user1')
        users_info = get_users_info()

    for user in users_info:
        print_user_info(user)


if __name__ == '__main__':
    main()
