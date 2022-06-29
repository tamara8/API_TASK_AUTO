import unittest
from Config.config import BASE_URI
from utils.request import apis


class Test (unittest.TestCase):
   def test_read_all_data(self):
        get_1 = apis.get_request(BASE_URI + "/posts")
        self.assertEquals(get_1, '200')


   def test_read_one_of_data(self):
        get_2 = apis.get_request(BASE_URI + "/posts/1")
        self.assertEquals(get_2, '200')


   def test_read_special_one_of_data(self):
        get_3 = apis.get_request(BASE_URI + "/comments?postId=1")
        self.assertEquals(get_3, '200')


   def test_create_new_person(self):
        post = apis.post_request("../utils/data/package.json", BASE_URI + "/posts")
        self.assertEquals(post, '201')


   def test_delete_user(self):
        delete = apis.delete_request(BASE_URI + "/posts/1")
        self.assertEquals(delete, '200')


   def test_negative_for_delete_user_from_unvalid_request(self):
       delete = apis.delete_request(BASE_URI + "/posts/1/5")
       self.assertEquals(delete, '404')

   def test_negative_for_get_data_from_unvalid_request(self):
        get_1 = apis.get_request(BASE_URI + "/user")
        self.assertEquals(get_1, '404')

   def test_negative_for_create_user_from_unvalid_request(self):
        post = apis.post_request("../utils/data/package.json", BASE_URI + "/user/hg")
        self.assertEquals(post, '404')
