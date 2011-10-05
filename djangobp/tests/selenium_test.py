#import unittest
#from djangobp.selenium import discover_suites, SeleniumTestCase
#from os.path import dirname
#
#class RunnerTest(unittest.TestCase):
#    def test_list_suites(self):
#        suites = discover_suites(dirname(__file__) + '/spec')
#        self.assertEqual(3, len(suites))
#        self.assertTrue(dirname(__file__) + '/spec/a/suite.html' in suites)
#        
#    def test_execute_html(self):
#        test = SeleniumTestCase(dirname(__file__) + '/spec/a/test1.html')
#        test.run
#        