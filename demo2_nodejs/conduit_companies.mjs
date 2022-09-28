import axios from 'axios'

const CONDUIT_API_URL = 'https://api.getconduit.app'
const CONDUIT_API_KEY = ' place your api key here '

const axiosInstance = axios.create({
    baseURL: CONDUIT_API_URL,
    headers: {accept: 'application/json'},
})

async function appRequest(endpoint, method = 'POST', data = {}) {
    return axiosInstance.request({
        url: endpoint,
        method: method,
        data: data,
        headers: {Authorization: `Bearer ${CONDUIT_API_KEY}`},
    })
}

async function companyRequest(endpoint, token, method = 'GET', params = {}) {
    return axiosInstance.request({
        url: endpoint,
        method: method,
        params: {token: token, ...params},
    })
}

/**
 * @typedef {{name: String, id: Number, native_id: String}} Account
 * @typedef {{name: String, id: Number, created_at: String, accounts: Account[]}} Credentials
 * @typedef {{id: String, name: String, credentials: Credentials[]}} Connection
 * @typedef {{
 * id: String,
 * name: String,
 * created_at: String,
 * link_page: Object.<{url: String, enabled: Boolean}>,
 * api_token: Object.<{token: String, expires_at: Number}>,
 * connections: Connection[]}} Company
 */

/**
 *
 * Gets a list of companies.
 * @constructor
 * @returns {Promise.<Company[]>} list of companies
 */
async function getCompanies() {
    let response = await appRequest('link/company/?include_connections=true', 'GET')
    return response.data
}

/**
 *
 * Creates company.
 * @constructor
 * @param {String}  companyId - company UUID.
 * @param {String}  name - company name.
 * @param {Boolean}  pageEnabled - initial link page state.
 * @returns {Promise.<Object.<{id: String, name:String, page_enabled: Boolean}>>} created company.
 */
async function createCompany(companyId, name, pageEnabled) {
    let response = await appRequest('link/company/', 'POST', {
        id: companyId,
        name: name,
        page_enabled: pageEnabled
    })
    return response.data
}

/**
 *
 * Creates company.
 * @constructor
 * @param {String}  companyToken - a company token.
 * @param {String}  integration - integration id.
 * @returns {Promise.<String>} Connect URL.
 */
async function getCompanyConnectIntegrationURL(companyToken, integration) {
    let response = await companyRequest(`link/credentials/connect/${integration}/`, companyToken, 'GET')
    return response.data.url
}


export { createCompany, getCompanies, getCompanyConnectIntegrationURL }
