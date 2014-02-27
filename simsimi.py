# -*- coding:utf-8 -*-

import requests
from urllib import urlencode

WEB_CHAT_URL = 'http://www.simsimi.com/func/req?lc=ch&msg=%s'
API_CHAT_URL = 'http://api.simsimi.com/request.p?key=%s&lc=ch&ft=1.0&text=%%s'
WEB_TECH_URL = 'http://www.simsimi.com/func/teach'


class SimSimiChat(object):

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.session = requests.Session()
        self.chat_url = API_CHAT_URL % self.api_key if self.api_key else WEB_CHAT_URL

    def chat(self, message):
        try:
            response = self.session.get(self.chat_url % urlencode([('', message)]))
            answer = response.json()
            if answer.get('result') == 100:
                reply = answer['response'].encode('utf-8')
            elif answer.get('result') == 404:
                reply = "你 TMD 能给说一句我能理解的么!!"
            else:
                reply = "我好像生病了"
        except Exception:
            reply = "我病入膏肓, XD"
        return reply

    def tech(self, req, resp):
        params = {'lc': 'ch', 'req': req, 'resp': resp}
        response = self.session.post(WEB_TECH_URL, params=params)
        return response.json()['result']
