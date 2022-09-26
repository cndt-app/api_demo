import axios from 'axios'

const CONDUIT_API_URL = 'https://api.getconduit.app'
const CONDUIT_CUSTOMER_API_KEY = '624d145f8b1841a4a3f2ea0454aebb83'

async function httpGet(endpoint, params = {}) {
    let client = axios.create({
        baseURL: CONDUIT_API_URL,
        headers: {accept: 'application/json'},
    })
    params.token = CONDUIT_CUSTOMER_API_KEY
    return client.get(endpoint, {params: params})
}


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
    let response = await httpGet('link/credentials/')
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
 * @param {Date}  dateFrom - starting date.
 * @param {Date}  dateTo - ending date.
 * @param {Number}  account - if set returns data urls for this account only.
 * @returns {Promise.<Object.<{String, Chunks}>>} lists of data chunks grouped by theirs data schema
 */
async function getDataChunks(integration, dateFrom, dateTo, account) {
    let params = {
        integration: integration,
        dateFrom: dateFrom,
        dateTo: dateTo,
        account: account,
    }
    let response = await httpGet('link/data_lake/', params)
    return response.data
}


export { getDataChunks, getCredentials }
