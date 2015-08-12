'''
'''

import diamond.collector
import httplib
import json

class CarbonCollector(diamond.collector.Collector):
    def __init__(self, *args, **kwargs):
        self._predata = None
        super(CarbonCollector, self).__init__(*args, **kwargs)

    def get_default_config(self):
        config = super(CarbonCollector, self).get_default_config()
        config.update({
            'path': 'carbon',
            'exclude': [],
            'gauge': []
        })
        return config

    def entries(self):
        conn = httplib.HTTPConnection("127.0.0.1:8888")
        conn.request("GET", "/entries")
        response = conn.getresponse()
        data = response.read()
        response.close()
        return json.loads(data)

    def isgauge(self, path):
        for gauge in self.config['gauge']:
            self.log.debug('gauge: %s'%gauge)
            if gauge in path:
                return True

        return False

    def walk(self, parent, pre, prefix=''):
        for k in parent:
            if k in self.config['exclude']:
                self.log.debug('%s is excluded'%k)
                continue
            data = parent[k]
            if prefix:
                path = prefix+'.'+k
            else:
                path = k
            if isinstance(data, str) or isinstance(data, unicode):
                try:
                    if self.isgauge(path):
                        self.log.debug('%s is gauge'%path)
                        self.publish(path, float(data))
                    else:
                        cnt = float(data) - float(pre[k])
                        self.log.debug('%s:%f %f %f'%(path, cnt, float(data), float(pre[k])))
                        if k == 'elapsed':
                            exec_cnt = float(parent['exec']) - float(pre['exec'])
                            if exec_cnt > 0:
                                self.publish(path, cnt / exec_cnt)
                        else:
                            if cnt >= 0:
                                self.publish(path, cnt)
                except ValueError:
                    self.log.exception('%s %s'%(path, data))
            elif isinstance(data, dict):
                self.walk(data, pre[k], path)


    def collect(self):
        collected = self.entries()
        if self._predata:
            self.walk(collected['module'], self._predata['module'])
        self._predata = collected
