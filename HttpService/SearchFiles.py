__author__ = 'shixk'

import os
import re
import json
import time
import datetime

class SearchFiles(object):

    dirpath = ''
    filter = ''
    filetype = []

    def __init__(self, serverinfo):
        self.dirpath = serverinfo['dirpath']
        self.filetype = ['.' + q for q in serverinfo['filetype'].split(',')]

    def getfileno2t(self):
        dirlist = os.listdir(self.dirpath)
        filelist = []
        for d in dirlist:
            filepath = os.path.join(self.dirpath, d)
            ftype = os.path.splitext(d)[1]
            ftime = time.strftime("%Y-%m-%d", time.localtime(os.path.getctime(filepath)))
            fctime = datetime.datetime.strptime(ftime, "%Y-%m-%d")
            filetime = datetime.datetime.strftime(fctime, "%Y-%m-%d")
            '''if os.path.isdir(filepath):
                continue
            elif ftype in filetype:'''
            if os.path.isdir(filepath):
                ftype = 'dir'
            else:
                ftype = re.search('\.(.+?)$', ftype).group(1)
            f = {
                "name": d,
                "size": os.path.getsize(filepath),
                "type": ftype,
                "path": filepath,
                "createtime": filetime,
                "modifytime": os.path.getmtime(filepath)
            }
            filelist.append(f)
        j = json.dumps(filelist)
        return j

    def getfilenotime(self, filetype):
        dirlist = os.listdir(self.dirpath)
        filelist = []
        if filetype == None:
            filetype = self.filetype
        for d in dirlist:
            filepath = os.path.join(self.dirpath, d)
            ftype = os.path.splitext(d)[1]
            ftime = time.strftime("%Y-%m-%d", time.localtime(os.path.getctime(filepath)))
            fctime = datetime.datetime.strptime(ftime, "%Y-%m-%d")
            filetime = datetime.datetime.strftime(fctime, "%Y-%m-%d")
            if os.path.isdir(filepath):
                continue
            elif ftype in filetype:
                f = {
                    "name": d,
                    "size": os.path.getsize(filepath),
                    "path": filepath,
                    "createtime": filetime,
                    "modifytime": os.path.getmtime(filepath)
                }
                filelist.append(f)
        j = json.dumps(filelist)
        return j

    def getfilelist(self, start, end, filetype):
        dirlist = os.listdir(self.dirpath)
        filelist = []
        if isinstance(start, str):
            start = datetime.datetime.strptime(start, "%Y-%m-%d")
        if isinstance(end, str):
            end = datetime.datetime.strptime(end, "%Y-%m-%d")
        if filetype == None:
            filetype = self.filetype
        for d in dirlist:
            filepath = os.path.join(self.dirpath, d)
            ftype = os.path.splitext(d)[1]
            ftime = time.strftime("%Y-%m-%d", time.localtime(os.path.getctime(filepath)))
            fctime = datetime.datetime.strptime(ftime, "%Y-%m-%d")
            filetime = datetime.datetime.strftime(fctime, "%Y-%m-%d")
            if os.path.isdir(filepath):
                continue
            elif ftype in filetype:
                if (fctime >= start) and (fctime <= end):
                    f = {
                        "name": d,
                        "size": os.path.getsize(filepath),
                        "path": filepath,
                        "createtime": filetime,
                        "modifytime": os.path.getmtime(filepath)
                    }
                    filelist.append(f)
        j = json.dumps(filelist)
        return j

    def getfileno_type(self, start, end):
        dirlist = os.listdir(self.dirpath)
        filelist = []
        if isinstance(start, str):
            start = datetime.datetime.strptime(start, "%Y-%m-%d")
        if isinstance(end, str):
            end = datetime.datetime.strptime(end, "%Y-%m-%d")
        for d in dirlist:
            filepath = os.path.join(self.dirpath, d)
            ftype = os.path.splitext(d)[1]
            ftime = time.strftime("%Y-%m-%d", time.localtime(os.path.getctime(filepath)))
            fctime = datetime.datetime.strptime(ftime, "%Y-%m-%d")
            filetime = datetime.datetime.strftime(fctime, "%Y-%m-%d")
            #elif ftype in filetype:
            if (fctime >= start) and (fctime <= end):
                print ftype
                if os.path.isdir(filepath):
                    ftype = 'dir'
                else:
                    ftype = re.search('\.(.+?)$', ftype).group(1)
                f = {
                    "name": d,
                    "size": os.path.getsize(filepath),
                    "path": filepath,
                    "type": ftype,
                    "createtime": filetime,
                    "modifytime": os.path.getmtime(filepath)
                }
                filelist.append(f)
        j = json.dumps(filelist)
        return j