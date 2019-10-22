import requests
import unittest
from jiekou.common import con_mysql,execute_sql,close,get_time,url_base
from jiekou.base_data import get_data
mark = 0
class test_ad(unittest.TestCase):
    def setUp(self):
        self.url = url_base()+'add_guest/'
        self.con, self.cur = con_mysql()
    def tearDown(self):
        global mark
        mark += 1
    def test_1(self):
        '''添加嘉宾'''
        f = get_data()
        self.data = {}
        self.data['eid'] = 1216
        self.data['realname'] = f.get_name()
        self.data['phone'] = f.get_num(13111111111,13999999999)
        r = requests.post(self.url, self.data)
        self.con.autocommit(True)
        res = r.json()
        print(res)
        sql = 'select * from sign_guest where realname="%s";'
        select_result = self.cur.execute(sql % (self.data['realname']))
        try:
            self.assertEqual(res['message'],'add guest success')
            self.assertEqual(res['status'],10000)
            self.assertEqual(select_result,1)
        except:
            print('fail')
            raise Exception
        else:
            print('pass')
        close(self.con,self.cur)
    def test_2(self):
        '''不输入eid添加嘉宾失败'''
        n = 'caiji2'
        self.data = {}
        self.data['realname'] = n
        self.data['phone'] = 13777777711
        r = requests.post(self.url, self.data)
        res = r.json()
        try:
            self.assertEqual(res['message'],'parameter error')
            self.assertEqual(res['status'],10021)
        except:
            print('fail')
        else:
            print('pass')
    def test_3(self):
        '''输入不存在的eid添加嘉宾失败'''
        n = 'caiji2'
        self.data = {}
        self.data['eid'] = 1278
        self.data['realname'] = n
        self.data['phone'] = 13777777711
        r = requests.post(self.url, self.data)
        res = r.json()
        print(res)
        try:
            self.assertEqual(res['message'], 'event id null')
            self.assertEqual(res['status'], 10022)
        except:
            print('fail')
        else:
            print('pass')
    def test_4(self):
        '''输入status为0的发布会添加嘉宾失败'''
        n = 'caiji2'
        self.data = {}
        self.data['eid'] = 1214
        self.data['realname'] = n
        self.data['phone'] = 13777777711
        r = requests.post(self.url, self.data)
        res = r.json()
        print(res)
        try:
            self.assertEqual(res['message'], 'event status is not available')
            self.assertEqual(res['status'], 10023)
        except:
            print('fail')
        else:
            print('pass')
    def test_5(self):
        '''发布会人数已满添加嘉宾失败'''
        n = 'caiji2'
        self.data = {}
        self.data['eid'] = 1212
        self.data['realname'] = n
        self.data['phone'] = 13777777711
        r = requests.post(self.url, self.data)
        res = r.json()
        print(res)
        try:
            self.assertEqual(res['message'], 'event number is full')
            self.assertEqual(res['status'], 10024)
        except:
            print('fail')
        else:
            print('pass')
    def test_6(self):
        '''发布会已经开始添加嘉宾失败'''
        n = 'caiji2'
        self.data = {}
        self.data['eid'] = 1216
        self.data['realname'] = n
        self.data['phone'] = 13777777711
        r = requests.post(self.url, self.data)
        res = r.json()
        print(res)
        try:
            self.assertEqual(res['message'], 'event has started')
            self.assertEqual(res['status'], 10025)
        except:
            print('fail')
        else:
            print('pass')
    def test_7(self):
        '''手机号重复添加嘉宾失败'''
        n = 'caiji2'
        self.data = {}
        self.data['eid'] = 1216
        self.data['realname'] = n
        self.data['phone'] = 13880089439
        r = requests.post(self.url, self.data)
        res = r.json()
        print(res)
        try:
            self.assertEqual(res['message'], 'the event guest phone number repeat')
            self.assertEqual(res['status'], 10026)
        except:
            print('fail')
        else:
            print('pass')
    def test_8(self):
        '''手机号错误添加嘉宾失败'''
        n = 'caiji2'
        self.data = {}
        self.data['eid'] = 1216
        self.data['realname'] = n
        self.data['phone'] = 1388008943
        r = requests.post(self.url, self.data)
        res = r.json()
        print(res)
        try:
            self.assertEqual(res['message'], 'phone errort')
            self.assertEqual(res['status'], 10027)
        except:
            print('fail')
        else:
            print('pass')
if __name__ == '__main__':
    unittest.main()
