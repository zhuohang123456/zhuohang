import requests
import unittest
from jiekou.common import con_mysql,execute_sql,close,get_time,url_base
from jiekou.base_data import get_data
mark = 0
class test_em(unittest.TestCase):
    def setUp(self):
        self.url = url_base()+'sec_get_event_list/'
    def tearDown(self):
        global mark
        mark += 1
    def test_1(self):
        '''带认证查询发布会'''
        self.data = {}
        self.data['eid'] = 1216
        r = requests.get(self.url,self.data,auth = ('hanghang', 'zhuohang'))
        res = r.json()
        self.con, self.cur = con_mysql()
        sql = 'select * from sign_event where id="%d";'
        select_result = self.cur.execute(sql % (self.data['eid']))
        try:
            self.assertEqual(res['message'], 'success')
            self.assertEqual(res['status'], 200)
            self.assertEqual(select_result, 1)
        except:
            print('fail')
        else:
            print('pass')
        close(self.con, self.cur)
    def test_2(self):
        '''用户名不存在导致认证失败查询失败'''
        self.data = {}
        self.data['eid'] = 1216
        r = requests.get(self.url,self.data)
        res = r.json()
        self.con, self.cur = con_mysql()
        try:
            self.assertEqual(res['message'], 'user auth null')
            self.assertEqual(res['status'], 10011)
        except:
            print('fail')
        else:
            print('pass')
    def test_3(self):
        '''用户名密码错误导致认证失败查询失败'''
        self.data = {}
        self.data['eid'] = 1216
        r = requests.get(self.url,self.data,auth = ('hanghang', 'zhuohang1'))
        res = r.json()
        self.con, self.cur = con_mysql()
        try:
            self.assertEqual(res['message'], 'user auth fail')
            self.assertEqual(res['status'], 10012)
        except:
            print('fail')
        else:
            print('pass')
    def test_4(self):
        '''eid和name均不输入查询失败'''
        self.data = {}
        r = requests.get(self.url,self.data,auth = ('hanghang', 'zhuohang'))
        res = r.json()
        self.con, self.cur = con_mysql()
        try:
            self.assertEqual(res['message'], 'parameter error')
            self.assertEqual(res['status'], 10021)
        except:
            print('fail')
        else:
            print('pass')
    def test_5(self):
        '''未找到信息查询失败'''
        self.data = {}
        self.data['eid'] = 1288
        r = requests.get(self.url,self.data,auth = ('hanghang', 'zhuohang'))
        res = r.json()
        self.con, self.cur = con_mysql()
        try:
            self.assertEqual(res['message'], 'query result is empty')
            self.assertEqual(res['status'], 10022)
        except:
            print('fail')
        else:
            print('pass')
if __name__ == '__main__':
    unittest.main()