'''import requests
url = 'http://127.0.0.1:8000/api/get_event_list/'
data = {'eid':1212}
r = requests.get(url,data)
print(r.text)
res = r.json()
print(res)
print(res['message'])
print(r.status_code)
if res['status'] == 10000:
    print('pass')
else:
    print('fail')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
url = ('http://127.0.0.1:8000/api/add_event/')
data = {'eid':1289,'name':'花花舞台','limit':12,'status':1,'address':'成都','start_time':'2019-12-12 12:00:00'}
r = requests.post(url,data)
res = r.json()
print(res)
if res['message'] == 'add event success' and res['status'] == 10000:
    print('pass')
else:
    print('fail')'''