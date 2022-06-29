import requests
import json



class apis:
    @staticmethod
    def post_request(fileName,URL):
        with open(fileName,'r') as f:
         request_json = json.load(f)
        HEADERS = {'Content_Type': 'application/json'}
        r=requests.post(URL,request_json,headers=HEADERS)
        w1 = str(r.status_code)
        print(r.text)
        return w1

    @staticmethod
    def get_request(URL):
        HEADERS = {'Content_Type':'application/json'}
        r = requests.get(URL,headers=HEADERS)
        w= str(r.status_code)
        print(r.text)
        return w
        #print("**"+w+"**")



    @staticmethod
    def delete_request(URL):
        HEADERS = {'Content_Type':'application/json'}
        r = requests.delete(URL,headers=HEADERS)
        print(r.text)
        w2 = str(r.status_code)
        return w2

