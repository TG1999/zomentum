import json
import unittest
from server import app
from mock import patch, Mock, MagicMock, call, sentinel
from pymongo import MongoClient 
# from flask import *
db = MongoClient("mongodb+srv://tushar:VjD6w6cWZbvdSsy@cluster0.vxsjh.mongodb.net/test?retryWrites=true&w=majority")
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_book_right_ip(self):
        with patch('server.mongo_client') as mock:
            mock.return_value = db
            resp = self.app.post('api/book',json = {"timings":"01-10-2020-21:00:00","name":"Test","phone":"991"},content_type='application/json')
            self.assertEqual(resp.status_code, 200)
            content = json.loads(resp.get_data(as_text=True))
            self.assertEqual(content,{'res': 'Done'})
    
    def test_update_right_ip(self):
        with patch('server.mongo_client') as mock:
            mock.return_value = db
            resp = self.app.post('api/update',json = {"ticket":"5f4bbefeaf914233364e20ed","time":"01-10-2020-22:00:00"},content_type='application/json')
            self.assertEqual(resp.status_code, 200)
            content = json.loads(resp.get_data(as_text=True))
            self.assertEqual(content,{'res': 'updated'})

    def test_ticket_show(self):
        with patch('server.mongo_client') as mock:
            mock.return_value = db
            resp = self.app.post('api/tickets',json = {"time":"01-10-2020-20:00:00"},content_type='application/json')
            self.assertEqual(resp.status_code, 200)
            content = json.loads(resp.get_data(as_text=True))
            expected = {
    "res": [
        {
            "ticket": "5f4bbeffaf914233364e20ee",
            "user": "5f4bbefeaf914233364e20ed"
        },
        {
            "ticket": "5f4bccbf7f82c61e8dee5feb",
            "user": "5f4bccbf7f82c61e8dee5fea"
        },
        {
            "ticket": "5f4bcf580342ea1b6a1a6b43",
            "user": "5f4bcf580342ea1b6a1a6b42"
        },
        {
            "ticket": "5f4bcf590342ea1b6a1a6b45",
            "user": "5f4bcf590342ea1b6a1a6b44"
        },
        {
            "ticket": "5f4bcf839ef6ed408bdb4723",
            "user": "5f4bcf839ef6ed408bdb4722"
        },
        {
            "ticket": "5f4bcfa4f4466297051316ff",
            "user": "5f4bcfa4f4466297051316fe"
        },
        {
            "ticket": "5f4bd021f2d8c0879cddf6cc",
            "user": "5f4bd021f2d8c0879cddf6cb"
        },
        {
            "ticket": "5f4be178255a1db0b3714616",
            "user": "5f4be178255a1db0b3714615"
        },
        {
            "ticket": "5f4beb25faff5815e4057ee0",
            "user": "5f4beb25faff5815e4057edf"
        },
        {
            "ticket": "5f4bef71662ca4eb68410487",
            "user": "5f4bef71662ca4eb68410486"
        },
        {
            "ticket": "5f4befcf88cba0dabe98c6b2",
            "user": "5f4befce88cba0dabe98c6b1"
        },
        {
            "ticket": "5f4bf03090312d4ae0a3ca0a",
            "user": "5f4bf02f90312d4ae0a3ca09"
        },
        {
            "ticket": "5f4bf0cf6a680920f5ee5da7",
            "user": "5f4bf0ce6a680920f5ee5da6"
        },
        {
            "ticket": "5f4bf100e5527a7256c4cc75",
            "user": "5f4bf100e5527a7256c4cc74"
        },
        {
            "ticket": "5f4bf108cb3b35d2de945ca3",
            "user": "5f4bf108cb3b35d2de945ca2"
        },
        {
            "ticket": "5f4bf10e7cc9e9b9f338b4ff",
            "user": "5f4bf10e7cc9e9b9f338b4fe"
        },
        {
            "ticket": "5f4bf1316774f8086ad722ab",
            "user": "5f4bf1316774f8086ad722aa"
        }
    ]
}
            self.assertEqual(content,expected)

    def test_user_show(self):
        with patch('server.mongo_client') as mock:
            mock.return_value = db
            resp = self.app.post('api/user',json = {"ticket":"5f4bbeffaf914233364e20ee"},content_type='application/json')
            self.assertEqual(resp.status_code, 200)
            content = json.loads(resp.get_data(as_text=True))
            self.assertEqual({'res': {'_id': '5f4bbefeaf914233364e20ed', 'name': 'Test', 'phone': '991'}},content)
    
    def test_delete(self):
        with patch('server.mongo_client') as mock:
            mock.return_value = db
            resp = self.app.post('api/delete',json = {"ticket":"5f4bcd0febfd336f3d776cc1"},content_type='application/json')
            self.assertEqual(resp.status_code, 200)
            content = json.loads(resp.get_data(as_text=True))
            self.assertEqual({'res': 'Deleted'},content)
