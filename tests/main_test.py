# coding:utf-8

import unittest
from main import Main

class MainTest(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def test_first(self):
        print('test_first')

    def test_main(self):
        fuga = Main()
        self.assertTrue(main.index())


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(MainTest))
    return suite
