# -*- coding: utf-8 -*-
from http.client import ImproperConnectionState
import json
import transaction
import requests
import socket


class ConfigFunctions(object):
    DDCACHE_FOLDER = 'data_container'
    DDCACHE_CONFIG = 'config.json'
    fallback_info = {
        "broker": "192.168.178.85",
        "port": 1883,
        "topic": "hello",
        "client_id": "python-mqtt-1",
        "username": "pico",
        "password": "plantcare"
    }

    def __init__(self):
        self.read_config()

    # ---------------------------------------------------
    # return python dict as json formatted string
    # ---------------------------------------------------

    def get_config_as_string(self):
        json_formatted_str = json.dumps(self.config_json, indent=2)
        return json_formatted_str

    # ---------------------------------------------------
    # return json as python dict
    # ---------------------------------------------------

    def read_config(self):
        path = '/'+self.DDCACHE_FOLDER+'/'+self.DDCACHE_CONFIG
        try:
            target = self.context.unrestrictedTraverse(path)
            JsonData = json.loads(target.data)
        except:
            self.config_json = self.fallback_info
            self.update_config()
            JsonData = self.fallback_info
        try:
            x = self.getResponse('192.168.178.88')
            print(x)
        except:
            print("fehler!!!")
            """ """

        #y = self.getResponse('192.168.178.88')
        return JsonData

    # ---------------------------------------------------
    # Save json in folder data_container
    # 1) check if a Folder exists in ZODB (name = data_container)
    # 2) if not create
    # save json as file (config.json)
    # ---------------------------------------------------
    def update_config(self):
        if self.DDCACHE_FOLDER not in self.context.objectIds():
            transaction.begin()
            self.context.manage_addFolder(
                self.DDCACHE_FOLDER,
                title='Folder for Json Data'
            )
            transaction.commit()
        Folder = self.context.restrictedTraverse(self.DDCACHE_FOLDER)
        data = json.dumps(self.config_json).encode('utf-8')
        try:
            File = Folder.restrictedTraverse(self.DDCACHE_CONFIG)
            File.update_data(data)
        except:
            Folder.manage_addFile(id=self.DDCACHE_CONFIG, title=self.DDCACHE_CONFIG, file=data,
                                  content_type='application/json')

    def getResponse(self, ip):
        url = 'http://'+ip
        print(url)
        response = requests.get(url)
        return response.json()
        if response.status_code == requests.codes.ok:
            if 'application/json' in response.headers['Content-Type']:
                return response.json()
        return {'errors': ['StatusCode:'+str(response.status_code), 'CONTENTTYPE:'+response.headers['Content-Type']]}

    def get_my_ip(self):
        """
        Find my IP address
        :return:
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip