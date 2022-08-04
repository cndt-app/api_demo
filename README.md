# api_demo

## Setup

1. Install python 3.9;
2. Clone this repository;
3. use 'pip install requests' to install requirements.

## demo1

A command line Conduit Link API demo client.

Place your API key to CONDUIT_CUSTOMER_API_KEY constant in `conduit_link.py`.

Run `python main.py`

The script will parse all your connections and download data for a week.

## demo2

A command line users management Conduit Link API demo client.

This client requires Conduit API key to gain access.
Place your API key to CONDUIT_API_KEY constant in `conduit_users.py`.

Run `python main.py`

The script will print a list of all users and their connections.
If you don't have any users the script will create one for you.
