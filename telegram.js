const axios = require('axios');


const text = 'msg'
const url = `https://api.telegram.org/bot844196965:AAFZ89fz9u-cJDtQYsAzaiRmH77omoIc6Po/sendMessage?chat_id=628537753&text=${text}`
axios.get(url);