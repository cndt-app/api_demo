# A command line Conduit Link API demo client.

## Setup

1. Install nodejs and npm;
2. Clone this repository;
3. use 'npm install' to install dependencies.

### Application API key

This client requires Conduit API key to gain access.

You can obtain your API key at Conduit developers portal:
1. Open https://app.getconduit.app;
2. Find `Developers` link in the left navigation sidebar and click on it;
3. You'll be redirected to the developers portal https://developers.getconduit.app/;
4. Click on `Link Apps` link in the left navigation sidebar;
5. Create your application there and copy its key.

Place your API key to CONDUIT_API_KEY constant in `conduit_companies.py`.

### Usage

Run `npm run start`

The script will print a list of all companies and their connections.
If you don't have any companies - the script will create one for you.
