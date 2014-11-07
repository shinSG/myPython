__author__ = 'shixk'

import datetime
from SearchFiles import SearchFiles

class GetData(object):
    def loadfilterdata(self, query, conf):
        if query['method'] == "time":
            return self.filterbydate(query, conf)
        else:
            return {'ERROR': 'no method'}

    def filterbydate(self, query, conf):
        sf = SearchFiles(conf)
        global file_list
        if 'filetype' in query.keys():
            query['filetype'] = ['.' + q for q in query['filetype'].split(',')]
            if 'start' not in query.keys():
                file_list = sf.getfilenotime(query['filetype'])
                return file_list
            elif 'end' not in query.keys():
                query['end'] = datetime.datetime.strptime(query['start'], "%Y-%m-%d") + datetime.timedelta(hours=24)
            file_list = sf.getfilelist(query['start'], query['end'], query['filetype'])
        else:
            if 'start' not in query.keys():
                file_list = sf.getfileno2t()
                return file_list
            elif 'end' not in query.keys():
                query['end'] = datetime.datetime.strptime(query['start'], "%Y-%m-%d") + datetime.timedelta(hours=24)
            file_list = sf.getfileno_type(query['start'], query['end'])
        return file_list