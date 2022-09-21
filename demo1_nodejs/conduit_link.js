const axios = require('axios').default;

CONDUIT_API_URL = 'https://api.getconduit.app'
CONDUIT_CUSTOMER_API_KEY = ' place your api key here '

/**
 * @typedef {{name: String, id: Number, native_id: String}} Account
 * @typedef {{name: String, id: Number, created_at: String, accounts: Account[]}} Credentials
 */

/**
 *
 * Gets a list of data chunks for the given integration, account and date range.
 * @constructor
 * @returns {Promise.<Array.<{id: String, name: String, credentials: Credentials[]}>>} list of integrations
 */
async function getCredentials() {
    let response = await request('link/credentials/')
    return response.data
}

/**
 * @typedef {{service_status: String, data_status: String, data_updated_at: String}} Chunk
 * @typedef {Chunk[]} Chunks
 */

/**
 * Gets a list of data chunks for the given integration, account and date range.
 * @constructor
 * @param {String}  integration - integration unique name.
 * @param {Date}  date_from - starting date.
 * @param {Date}  date_to - ending date.
 * @param {Number}  account - if set returns data urls for this account only.
 * @returns {Promise.<Object.<{String, Chunks}>>} lists of data chunks grouped by theirs data schema
 */
async function getDataChunks(integration, date_from, date_to, account) {
    let params = {
        integration: integration,
        date_from: date_from,
        date_to: date_to,
        account: account
    }
    let response = await request('link/data_lake/', params)
    return response.data
}

async function request(endpoint, params = {}) {
    params.token = CONDUIT_CUSTOMER_API_KEY
    let fullPath = new URL(endpoint, CONDUIT_API_URL).href
    let headers = {
        'accept': 'application/json',
    }
    return axios.get(fullPath, {headers: headers, params: params})
}

module.exports = {getDataChunks, getCredentials}