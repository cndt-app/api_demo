# api_demo

## Setup

1. Install python 3.9;
2. Clone this repository;
3. use 'pip install requests' to install requirements.

## demo1

A command line Conduit Link API demo client.

### Customer API key

This client requires Conduit customer API key to gain access.

You can obtain your API key at Conduit developers portal:
1. Open https://app.getconduit.app;
2. Find `Developers` link in the left navigation sidebar and click on it;
3. You'll be redirected to the developers portal https://developers.getconduit.app/;
4. You can get your API key on `Home` page.

Place your API key to CONDUIT_CUSTOMER_API_KEY constant in `conduit_link.py`.

### Usage

Run `python main.py`

The script will parse all your connections and download data for a week.

## demo2

A command line users management Conduit Link API demo client.

### Application API key

This client requires Conduit API key to gain access.

You can obtain your API key at Conduit developers portal:
1. Open https://app.getconduit.app;
2. Find `Developers` link in the left navigation sidebar and click on it;
3. You'll be redirected to the developers portal https://developers.getconduit.app/;
4. Click on `Link Apps` link in the left navigation sidebar;
5. Create your application there and copy its key.

Place your API key to CONDUIT_API_KEY constant in `conduit_users.py`.

### Usage

Run `python main.py`

The script will print a list of all users and their connections.
If you don't have any users the script will create one for you.
