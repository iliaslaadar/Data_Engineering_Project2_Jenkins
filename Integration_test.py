#!/usr/bin/env python
# coding: utf-8


import unittest
import requests
import os


class Test_integration(unittest.TestCase):
    
    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        
        
    def tearDown(self):
        pass
    
    
    def test_a_index(self):
        responce = requests.get('http://localhost:5000')
        self.assertEqual(responce.status_code, 200)
    
    
    def test_preprocess(self):
        data_ = {
            'text': "We are / checkinG unit test?",
            'form_type': 'analyse'
        }
        responce = requests.post('http://localhost:5000/', data=data_)
        self.assertEqual(responce.status_code, 200)
        #self.assertIn('checking unit test'.encode(),responce.content)
        
        
    def test_top_tweet(self):
        data_ = {
            'text': "@tristanmf: @realDonaldTrump Trump for president ! Trump for America ! #Trump2016",
            'form_type': 'analyse'
        }
        responce = requests.post('http://localhost:5000/', data=data_)
        self.assertEqual(responce.status_code, 200)
        
        
if __name__ == '__main__':
    unittest.main()
