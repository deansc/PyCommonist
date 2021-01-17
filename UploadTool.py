import json, requests
from constants import URL_TOKEN, \
    URL_LOGIN, \
    URL_LOGIN2

class UploadTool:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.token = ''
        self.cookies = ''

    def connect(self):
        try:
            ret = requests.get(URL_TOKEN)
            retToken = json.loads(ret.content)
            #print(retToken)
            self.token = retToken['query']['tokens']['logintoken']
            self.cookies = ret.cookies

            urlLogin = URL_LOGIN + self.login + URL_LOGIN2
            paramsLogin = {'password' : self.password, 'logintoken': self.token}
            r = requests.post(urlLogin, paramsLogin, cookies=self.cookies)
            ret = True
        except:
            ret = False
        return ret

    def uploadImages(self, widget):
        print("yolo")
