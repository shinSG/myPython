__author__ = 'shixk'

import re
import urlparse
from GetData import GetData
from BaseHTTPServer import BaseHTTPRequestHandler

class ServConf:
    conf = {}
    def __init__(self):
        self.conf = self.initconf()

    def initconf(self):
        f = open('conf/server.conf', 'r')
        pramalist = f.readlines()
        prama = {}
        for p in pramalist:
            key = re.search("(.+?)=", p).group(1)
            try:
               tempvalue = re.search('=(.+?)\n', p)
               if tempvalue:
                   value = tempvalue.group(1)
               else:
                   value = re.search('=(.+?)$', p).group(1)
            except:
                pass
            prama[key] = value
        return prama


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.request_handler("GET")

    def do_POST(self):
        self.request_handler("POST")

    def request_handler(self, type):
        if type == 'GET':
            path = urlparse.urlparse(self.path)
            isparam = re.search('\?', self.path)
            querystr = path.query
            query = {}
            if isparam:
                for q in querystr.split('&'):
                    key = q.split('=')[0]
                    value = q.split('=')[1]
                    query[key] = value
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                e = GetData()
                filejson = e.loadfilterdata(query, ServConf().initconf())
                self.wfile.write(filejson)
            else:
                self.send_error(400)
#        else: