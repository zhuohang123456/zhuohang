'''import requests
url = 'http://192.168.1.29:9000/api/login/'
data = {'username':'admin','password':'sys123456'}
rep = requests.post(url=url,data=data)
rep = rep.json()
print(rep)
token = rep['token']
url = 'http://192.168.1.29:9000/api/card/'
data = {'card_id':'61234568','card_user':'张三'}
header = {'Authorization':'Token '+token}
rep = requests.post(url=url,headers=header,data=data)
rep = rep.json()
print(rep)'''