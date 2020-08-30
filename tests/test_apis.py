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
            resp = self.app.post('api/book',json = {"timings":"01-10-2020-20:00:00","name":"Test","phone":"991"},content_type='application/json')
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
            resp = self.app.post('api/tickets',json = {"time":"01-10-2020-21:00:00"},content_type='application/json')
            self.assertEqual(resp.status_code, 200)
            content = json.loads(resp.get_data(as_text=True))
            expected = {
                # {'res': {'_id': '5f4bf57d843435223eedb5c0', 'name': 'Test', 'phone': '991'}}
                'res': [{'ticket': '5f4bf54a78b9ebdd80c73f20',
 'user': '5f4bf54a78b9ebdd80c73f1f'},
{'ticket': '5f4bf57d843435223eedb5c1',
 'user': '5f4bf57d843435223eedb5c0'},
{'ticket': '5f4bf6199e11715e3b64d2e9',
 'user': '5f4bf6199e11715e3b64d2e8'},
{'ticket': '5f4bf65f22f1bd8ebb310bc9',
 'user': '5f4bf65f22f1bd8ebb310bc8'}]
            }

            self.assertEqual(content,expected)

    def test_user_show(self):
        with patch('server.mongo_client') as mock:
            mock.return_value = db
            resp = self.app.post('api/user',json = {"ticket":"5f4bf57d843435223eedb5c1"},content_type='application/json')
            self.assertEqual(resp.status_code, 200)
            content = json.loads(resp.get_data(as_text=True))
            self.assertEqual({'res': {'_id': '5f4bf57d843435223eedb5c0', 'name': 'Test', 'phone': '991'}},content)
    
    def test_delete(self):
        with patch('server.mongo_client') as mock:
            mock.return_value = db
            resp = self.app.post('api/delete',json = {"ticket":"5f4bcd0febfd336f3d776cc1"},content_type='application/json')
            self.assertEqual(resp.status_code, 200)
            content = json.loads(resp.get_data(as_text=True))
            self.assertEqual({'res': 'Deleted'},content)
