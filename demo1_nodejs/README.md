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

# Step by step

### Предварительный этап

Создать новый проект
`npm init`

Установить бибилотеку для http запросов
`npm install axios`

Добавить команду запуска в `package.json`

```
"scripts": {
    "main": "node index.js"
},
```

После этих шагов файл package.json должен выглядить примерно так:

```json
{
  "name": "demo1_nodejs",
  "version": "1.0.0",
  "description": "Conduit Link Api Demo",
  "main": "index.js",
  "scripts": {
    "main": "node index.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "axios": "^0.27.2",
    "moment": "^2.29.4"
  }
}
```

Создать файл `index.js`

### Запросы к апи

Для отправки запросов можно использовать любую бибилотеку для http запросов.
В качстве примера рассмотрим отправку при помощи одной из самых популярных библиотек - axios.

Для запроса к эндпоинту важно передать:

1) Заголовок `accept': 'application/json`
2) [Токен разработчика](#customer-api-key)), как query параметр `?token=your_token_here`


#### Подготовка

Для начала подготовим основу.
Импортируем библиотеку и создадим асинхронную функцию верхнего уровня

```js 
const axios = require("axios");

(async () => {
    // All code goes here
})()
```

#### Обращение к эндпоинту

Обращение к эндпоинту `/link/credentials/` будет выглядеть следующим образом:

```js
let response = await axios.get(
    'https://api.getconduit.app/link/credentials/', {
        headers: {accept: 'application/json'},
        params: {token: 'your_token_here'},
    })
```

#### Обращение к эндпоинту с параметрами

Обращение к эндпоинту `/link/data_lake/` будет выглядеть следующим образом:

```js
let response = await axios.get(
    'https://api.getconduit.app/link/data_lake/', {
        headers: {accept: 'application/json'},
        params: {
            token: 'your_token_here',
            integration: 'facebook_demo',
            date_from: '2022-09-02',
            date_to: '2022-09-08',
            account: 123,
        }
    })
```

##### DELETE запрос
Отправляются аналогично GET запросам, но вместо `axios.get`
необходимо вызывать `axios.delete`.

Пример:

```js
let response = await axios.delete(
    '/link/credentials/123/', {
        headers: {accept: 'application/json'},
    })
```

##### Обработка ошибок

```js
try {
    let response = await axios.get(
        'https://api.getconduit.app/link/credentials/', {
            headers: {accept: 'application/json'},
            params: {token: 'your_token_here'},
        })
} catch (e) {
    console.log(e)
}
```

##### Работа с ответом:

Вывод результата в консоль

```js
console.log(response.data)
```

Вывод списка credentials из ответа

```js
for (let integration of response.data) {
    console.log(`Integration: ${integration.name}`)
}
```

##### Полный код примера пример, работает as is:

Для запуска необходимо выполнить команду
`node index.js` где index.js - имя файла с кодом или `npm run main`

```js
const axios = require("axios");

(async () => {
    try {
        let response = await axios.get(
            'https://api.getconduit.app/link/credentials/', {
                headers: {accept: 'application/json'},
                params: {token: 'your_token_here'},
            })
        for (let integration of response.data) {
            console.log(`Integration: ${integration.name}`)
        }
    } catch (e) {
        console.log(e)
    }
})()
```

Результат выполнения:
![](./docs/run_result.png)

____

Полный список доступных эндпоинтов можно найти по адресу https://api.getconduit.app/