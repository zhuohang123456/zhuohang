import pymysql
import time
import csv,os  # 导入csv模块，用于处理csv格式文件
BASEPATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # 获取项目路径
CASEPATH = os.path.join(BASEPATH,'jiekou')    # 获取测试用例文件目录路径
IMGPATH = os.path.join(BASEPATH,'img')    # 获取截图文件目录路径
REPORTPATH = os.path.join(BASEPATH,'report')    # 获取测试报告文件目录路径
DATAPATH = os.path.join(BASEPATH,'data')     # 获取测试数据文件目录路径
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
def get_time():
    # 使用strftime()函数，按指定格式获取系统当前时间
    # %Y：4位年；%m：2位月；%d：2位天；%H：小时；%M：分钟；%S：秒
    hour = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    return hour
def url_base():
    return 'http://127.0.0.1:8000/api/'