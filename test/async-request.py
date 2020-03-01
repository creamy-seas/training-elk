import logging
from logstash_async.handler import AsynchronousLogstashHandler

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(AsynchronousLogstashHandler(
    'elkdreams-ai.com', 8080, database_path=None))

extra = {
    'message_type': 'execution_analysis',
    'Bank': 'ICBC',
    'Function Name': 'Yelp',
    'Success': True,
    'Parent List': ['test1', 'test2', 'test3'],
    'Account': 'bb56893',
    'End Point': True
}
logger.info('python-logstash: test extra fields', extra=extra)
