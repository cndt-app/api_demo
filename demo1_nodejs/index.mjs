import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'
import axios from 'axios'
import moment from 'moment'
import { getCredentials, getDataChunks } from './conduit_link.mjs'
const DATA_DIR = path.join(path.resolve(), 'data')

async function processDataChunks(integration_id, account, path_, date_range) {
    let [date_from, date_to] = date_range

    // Getting a list of data chunks
    let dataChunks = await getDataChunks(integration_id, date_from, date_to, account)

    for (let [schema, chunks] of Object.entries(dataChunks)) {
        for (let chunk of chunks) {
            console.log(
                `   ${chunk.date}: schema: ${schema} service_status: ${chunk.service_status}, ` +
                `data_status: ${chunk.data_status}, updated_at: ${chunk.data_updated_at}`
            )

            if (chunk.url) {
                await downloadDataChunk(chunk.url, path.join(path_, `${chunk.date}.csv`))
            }
        }
    }
}

async function downloadDataChunk(url, filename) {
    try {
        let response = await axios.get(url, {responseType: 'stream'})
        response.data.pipe(fs.createWriteStream(filename));
        console.log(`    ${response.headers['content-length']} bytes saved to file ${filename}`)
    } catch (e) {
        console.log(e)
    }
}

async function main(date_range) {
    //Getting a list of available integrations and theirs connected accounts
    let integrations = await getCredentials()

    for (let integration of integrations) {
        console.log(`Integration: ${integration.name}`)
        for (let credentials of integration.credentials) {
            console.log(` Credentials: ${credentials.id}:${credentials.name}, created at: ${credentials.created_at}`)
            for (let account of credentials.accounts) {
                console.log(`  Account: ${account.id}:${account.name}, native id: ${account.native_id}`)

                let path_ = path.join(DATA_DIR, integration.id, credentials.id.toString(), account.id.toString())
                fs.mkdirSync(path_, {recursive: true});

                await processDataChunks(integration.id, account.id, path_, date_range)
            }
        }
    }
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
    let date_range = [
        moment().subtract(6, 'days').format('YYYY-MM-DD'),
        moment().format('YYYY-MM-DD'),
    ]
    await main(date_range)
}




