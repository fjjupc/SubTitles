# -*- coding: utf-8 -*-

from requests import get
from json import loads

class ASSRT():
    def __init__(self, token) -> None:
        self.token = 'Bearer ' + token
        self.url_prefix = 'https://api.assrt.net/v1/'
        self.headers = {
            'Authorization': self.token
        }

    def download(self, id, dir):
        url = self.url_prefix + 'sub/detail'
        data = {
            'id': id
        }
        r = get(url, headers=self.headers, params=data, timeout=60)
        j = loads(r.text)
        if 'succeed' != j.get('sub').get('result'):
            return None
        subs = j.get('sub').get('subs')
        if 0 == len(subs):
            print('Got No Result!')
            return None
        download_url = subs[0].get('url')
        filename = subs[0].get('filename')
        filepath = dir + '/' + filename

        print('Now Download [%s] File To %s' % (download_url, filepath))
        r = get(download_url, timeout=120)
        with open(filepath, 'wb') as f:
            f.write(r.content)
        

    def getid(self, name):
        bFound = False
        url = self.url_prefix + 'sub/search'
        data = {
            'q': name,
            'no_muxer': '1'
        }
        r = get(url, headers=self.headers, params=data, timeout=60)
        if 200 != r.status_code:
            return None
        j = loads(r.text)
        if 'succeed' != j.get('sub').get('result'):
            return None
        subs = j.get('sub').get('subs')
        if 0 == len(subs):
            print('Got No Result!')
            return None
        for x in range(0, len(subs)):
            print('[%02d][%s]' % (x, subs[x].get('native_name')))
        while(True):
            num = int(input('Pleas Input Wich You Want to Download: '))
            if num >= 0 and num < len(subs):
                break
            else:
                print('Pleas input a valid number within 0 ~ %d' % len(subs) - 1)
        sub = subs[num]
        id = sub.get('id')
        return id

    def search(self, name, dir):
        id = self.getid(name)
        if id is None:
            return False
        self.download(id, dir)


