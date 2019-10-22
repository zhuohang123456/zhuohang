import requests
import unittest
from jiekou.common import con_mysql,execute_sql,close,get_time
from jiekou.base_data import get_data
class test_addevent(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/add_event/'
        f = get_data()
        self.data = {}
        self.data['eid'] = f.get_num(2000, 9999)
        self.data['name'] = 'iphone' + str(f.get_num(11, 99)) + '发布会'
        self.data['status'] = f.get_num(0, 1)
        self.data['limit'] = 200
        self.data['start_time'] = f.get_datetime()
        self.data['address'] = f.get_address()
    def tearDown(self):
        close(self.con, self.cur)
    def test_1(self):
        '''添加一个随机发布会'''
        r = requests.post(self.url,self.data)
        res = r.json()
        print(res)
        self.con, self.cur = con_mysql()
        sql = 'select * from sign_event where id="%d" and name="%s";'
        select_result = self.cur.execute(sql % (self.data['eid'], self.data['name']))
        if res['message'] == 'add event success' and res['status'] == 10000:
            print('pass')
        else:
            print('fail')

if __name__ == '__main__':
    unittest.main()


