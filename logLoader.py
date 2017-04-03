import time
import sys
from elasticsearch import Elasticsearch

def upload(url, filename, idx, dType):
    es = Elasticsearch([url], verify_certs=True)
    readF = open(filename)
    actions = ""
    
    for line in readF.read().split():
        if sys.getsizeof(actions) > 50000000:
            es.bulk(body=actions, index=idx, doc_type=dType)
            actions = ""
        actions += '{"index": {}}\n'
        actions += line + '\n'
    es.bulk(body=actions, index=idx, doc_type=dType)

####################################################################################################

start = time.time()

upload('http://elastic:changeme@localhost:9200/', '/home/da/20161027/post_26131000.log', 'data', 'log')

elapsed = time.time() - start
print(elapsed)