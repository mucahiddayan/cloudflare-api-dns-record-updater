#!/usr/bin/env python
# encoding: utf-8
# Author Muecahid Dayan <dayan.m@hotmail.de>

import requests

class CloudFlare:
    _apiUrl = "https://api.cloudflare.com/client/v4/zones/"
    def __init__(self, email, apikey,zone):
        self.apikey = apikey
        self.email = email
        self.zone = zone

    def _getIp(self):
        r=requests.get("https://ifconfig.co/json").json()
        return r['ip']

    def _getHeaders(self):
        return {"X-Auth-Key": self.apikey, "X-Auth-Email" : self.email}

    def _mergeRecords(self, r1,r2):
        copy = r1.copy()
        copy.update(r2)
        return copy

    def getDnsRecordsUri(self, id=''):
        return self._apiUrl + self.zone + '/dns_records/' + id


    def createRecord(self, record):
        return requests.post()

    def findRecordByName(self, name):
        r = self.listRecords()
        return filter(lambda record: record['name'] == name, r['result'] )

    def listRecords(self):
        return requests.get(self.getDnsRecordsUri(), headers=self._getHeaders()).json()

    def findRecordById(self, id):
        r = requests.get(self.getDnsRecordsUri(id), headers=self._getHeaders()).json()
        return r['result']

    def updateRecordById(self, id, newRecord):
        record = self.findRecordById(id)
        if record:
            return requests.put(self.getDnsRecordsUri(id), headers=self._getHeaders(), json=self._mergeRecords(record,newRecord)).json()
        else:
            print("No record with id: \"" + id + "\"")

    def updateRecordByName(self,name, newRecord):
        record = self.findRecordByName(name)
        if record:
            return self.updateRecordById(record[0]['id'], newRecord)
        else:
            print("No record with name: \"" + name + "\"")


    def updateRecordIpByName(self, name):
        ip = self._getIp()
        return self.updateRecordByName(name, {"content":ip})

    def updateRecordIpById(self, id):
        ip = self._getIp()
        return self.updateRecordById(id, {"content":ip})



