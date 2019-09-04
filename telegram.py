# https://api.telegram.org/bot<token>/<method>
    
    # https://api.telegram.org/bot844196965:AAFZ89fz9u-cJDtQYsAzaiRmH77omoIc6Po/getME 
    # https://api.telegram.org/bot844196965:AAFZ89fz9u-cJDtQYsAzaiRmH77omoIc6Po/getUpdates
    # https://api.telegram.org/bot844196965:AAFZ89fz9u-cJDtQYsAzaiRmH77omoIc6Po/sendMessage?chat_id=&text=

 #-*- coding:utf-8 -*-

import requests
from decouple import config

import sys

import io



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')





chat_id=''
text=''
base_url='https://api.telegram.org'
token=config('TOKEN')
print(token)


url = f'{base_url}/bot{token}/getUpdates'
# url ='https://api.telegram.org/bot844196965:AAFZ89fz9u-cJDtQYsAzaiRmH77omoIc6Po/getUpdates'
print(url)
# i=0

# for i in range(10):
#     requests.get(url)
res = requests.get(url)
# print(res.text)

data = res.json()
# res.json().key() => 키값이 무엇이 있는지 나옴
# print(data['result'])
print(data['result'][1]['message']['chat']['id'])
chat_id = data['result'][1]['message']['chat']['id']

#여러개가 있다.

senders = []
for result in data['result']:
    senders.append(result['message']['chat']['id'])
receivers = set(senders)
    print(receivers)
text= 'python 으로 보내는 메세지'
print(chat_id)
send_url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
print(send_url)


for r in receivers:
    send_url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
send_res = requests.get(send_url)
print(send_res)