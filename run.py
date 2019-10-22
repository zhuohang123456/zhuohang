import unittest
from jiekou.HTMLTestReportCN import HTMLTestRunner
from jiekou.common import get_time,REPORTPATH

datetime = get_time()
tests = unittest.defaultTestLoader.discover('')
f = open(REPORTPATH+'/'+'接口'+datetime + '.html', 'wb')
runner = HTMLTestRunner(stream = f,title = '接口自动化测试报告',tester = 'linlin')
runner.run(tests)
f.close()