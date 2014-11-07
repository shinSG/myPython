__author__ = 'shixk'

from BaseHTTPServer import HTTPServer
from SimpleServerService import RequestHandler, ServConf

def main():
    conf = ServConf()
    sconf = conf.initconf()
    server = HTTPServer((sconf['bind_ip'], int(sconf['port'])), RequestHandler)
    print 'started httpserver...'
    server.serve_forever()

if __name__ == '__main__':
    main()