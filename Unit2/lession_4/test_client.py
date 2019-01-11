# Программа клиента, запрашивающего текущее время
from socket import *
import unittest
import time, datetime


# from jim_client import get_timestamp
def get_timestamp():
    dt = datetime.datetime.now()
    # value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))
    # print(value.strftime('%Y-%m-%d %H:%M:%S'))
    return (dt)


def mockup_get_timestamp():
    return datetime.datetime.now()


class UnitTest1(unittest.TestCase):

    def setUp(self):
        self._get_start_time = datetime.datetime.now()
        self.get_local_time = time.ctime(time.time())
        self.get_srv_time = get_timestamp()

    def tearDown(self):
        elapsed = datetime.datetime.now() - self._get_start_time
        print('{} ({}s)'.format(self.id(), elapsed), "<= result")

    def test_should_run_fast(self):
        self.assertEqual(1, 1)

    def test_should_run_slow(self):
        time.sleep(1.5)
        self.assertEqual(1, 1)

    def test_year2019(self):
        self.assertRegex(self.get_local_time, "^.*2019$")

    def test_not_year2018(self):
        self.assertNotRegex(self.get_local_time, "^.*2018$")


if __name__ == '__main__':
    unittest.main()
