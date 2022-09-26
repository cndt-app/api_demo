# A command line Conduit Link API demo client.

## Setup

1. Install nodejs and npm;
2. Clone this repository;
3. use 'npm install' to install dependencies.

### Customer API key

This client requires Conduit customer API key to gain access.

You can obtain your API key at Conduit developers portal:
1. Open https://app.getconduit.app;
2. Find `Developers` link in the left navigation sidebar and click on it;
3. You'll be redirected to the developers portal https://developers.getconduit.app/;
4. You can get your API key on `Home` page.

Place your API key to CONDUIT_CUSTOMER_API_KEY constant in `conduit_link.js`.

### Usage

Run `npm run main`

The script will parse all your connections and download data for a week.
