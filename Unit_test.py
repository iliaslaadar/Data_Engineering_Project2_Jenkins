#!/usr/bin/env python
# coding: utf-8


import unittest
import model_dev


class Test_unit(unittest.TestCase):
    
    def test_preprocess(self):
        result = "We are / checkinG unit test?"
        res = "checking unit test"
        result2 = "This iS a second ' test to & check\ the result"
        res2 = "second test check result"
        
        self.assertEqual(model_dev.preprocess(result), res)
        self.assertEqual(model_dev.preprocess(result2), res2)
        
    def test_split_doc(self):
        result = ["we are checking unit test"]
        res = [['we', 'are', 'checking', 'unit', 'test']]
        result2 = ["this is a second test to check the result"]
        res2 = [['this', 'is', 'a', 'second', 'test', 'to', 'check', 'the', 'result']]
       
        self.assertEqual(model_dev.split_doc(result), res)
        self.assertEqual(model_dev.split_doc(result2), res2)
        
        
    def test_top_tweet(self):
        text = "@tristanmf: @realDonaldTrump Trump for president ! Trump for America ! #Trump2016"
        result = model_dev.top_tweets(1, text)
        res = '"@tristanmf: @realDonaldTrump Trump for president ! Trump for America ! #Trump2016"'

        self.assertEqual(result[0][0], res)
        
        
if __name__ == '__main__':
    unittest.main()
