import requests
from pprint import pprint as pp

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874'

res = requests.get(url)

# json을 python dictionary로 파싱
data = res.json()
pp(data)

winner = []


#js의 push 와 거의 동일 

for i in range(6):
    # range(1,7)도 가능
    j= i+1
    print(j)
    winner.append(data[f'drwtNo{j}'])
print (winner)