import { fileURLToPath } from 'url'
import { getCompanies, createCompany, getCompanyConnectIntegrationURL } from './conduit_companies.mjs'


async function printCompanyInfo(company) {
    console.log(`Company '${company.id}': created at: ${company.created_at}`)
    let companyToken = company.api_token.token
    let connectFacebookUrl = await getCompanyConnectIntegrationURL(companyToken, 'demo_facebook',)
    let connectGoogleAdsUrl = await getCompanyConnectIntegrationURL(companyToken, 'demo_google_ads',)


    let printData = {
        'Token': companyToken,
        'Link page': company.link_page.url,
        'Connect Demo Facebook URL:': connectFacebookUrl,
        'Connect Demo Google Ads URL': connectGoogleAdsUrl,
    }

    for (let [key, value] of Object.entries(printData)) {
        console.log(`\x1b[32m${key}: \x1b[0m`)
        console.log(value)
    }

    if (company.connections.length !== 0) {
        console.log('Connections: ')
        console.table(company.connections)
        for (let integration of company.connections) {
            console.log(`Integration: '${integration.name}' credentials`)
            console.table(integration.credentials)
            for (let credentials of integration.credentials) {
                console.log(`Credentials: '${credentials.name}' accounts`)
                console.table(credentials.accounts)
            }
        }
    }
    console.log('')
}

async function main() {
    let companies = await getCompanies()

    if (companies.length === 0) {
        await createCompany(`demo_company`, 'Demo Company', true)
        companies = await getCompanies()
    }

    for (let company of companies) {
        await printCompanyInfo(company)
    }
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
    await main()
}
