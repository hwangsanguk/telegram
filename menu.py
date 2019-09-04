# _ = require('lodash')

import random 

# const foods = ['피자','타코벨','장어','치킨']

foods = ['피자','타코벨','장어','치킨']

# console.log(_.sample(foods))
random.choice(foods)
print(random.choice(foods))


# 키벨류
matzip = {
    '백운봉 막국수':'이베리코 돼지고기',
    '고갯마루':'닭볶음탕',
    '대우식당':'부대찌개'
    }


# matzip.고갯마루  (x)
print(matzip['고갯마루'])