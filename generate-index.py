#!/usr/bin/python

import json
import cjson
import os

baseDir = os.path.dirname(os.path.realpath(__file__))
contentDir = os.path.join(baseDir, 'content')
jsonFile = os.path.join(baseDir, 'index.json');
cps = []
for fileName in os.listdir(contentDir):
    if '.vlcp' == os.path.splitext(fileName)[1]:
        f = open(os.path.join(contentDir, fileName))
        text = f.read();
        try:
            js = json.loads(text);
        except:
            # some of our json encoding is strange
            js = cjson.decode(text)
        js.pop('dashboardSections', None)
        js.pop('alerts', None)
        js.pop('queries', None)
        js.pop('eventTypes', None)
        js.pop('extractedFields', None)
        js['fileName'] = fileName
        cps.append(js)
f = open(jsonFile, 'w')
f.write(json.dumps(cps, indent=2, separators=(',', ': ')))
f.close()
