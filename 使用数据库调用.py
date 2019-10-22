import pymysql  #引入pymysql模块
import requests
from faker import Faker
class get_data():
    fake = Faker(locale='zh_CN')
    def get_num(self,m,n):
        return self.fake.random_int(min=m,max=n)
    def get_string(self):
        return self.fake.sentence()[:-1]
    def get_address(self):
        return self.fake.province()+'-'+self.fake.city()
    def get_datetime(self):
        return self.fake.future_datetime()
def con_mysql():
    con,cur = '',''
    try:
        con = pymysql.connect('localhost','root','root','learn',3306,charset='utf8')
    except:
        print('数据库连接错误')
    else:
        print('连接成功')
        cur = con.cursor()
    return con,cur
def execute_sql(cur,sql):
    return cur.execute(sql)
def close(con,cur):
    con.close()
    cur.close()
url = 'http://127.0.0.1:8000/api/add_event/'
f = get_data()
data = {}
data['eid'] = f.get_num(2000,9999)
data['name'] = 'iphone'+str(f.get_num(11,99))+'发布会'
data['status'] = f.get_num(0,1)
data['limit'] = 200
data['start_time'] = f.get_datetime()
data['address'] = f.get_address()
r = requests.post(url,data)
res = r.json()
print(res)
con,cur = con_mysql()
sql = 'select * from sign_event where id="%d" and name="%s";'
select_result = cur.execute(sql %(data['eid'],data['name']))
if res['message'] == 'add event success' and res['status'] == 10000:
    print('pass')
else:
    print('fail')
close(con,cur)







