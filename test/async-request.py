import requests
import logging
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.formatter import LogstashFormatter

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)


lg_formatter = LogstashFormatter(
    message_type='execution_analysis',
    extra_prefix='executiondoc')
lg_handler = AsynchronousLogstashHandler(
    'elkdreams-ai.com', 8080, database_path=None)
lg_handler.setFormatter(lg_formatter)

logger.addHandler(lg_handler)


extra = {
    'bank': 'ICBC',
    'function': 'Yelp',
    'trigger_function': True,
    'ancestor_functions': ['test1', 'test2', 'test3'],
    'success': True,
    'account': 'bb56893',
    'clientip': requests.get('http://ip.42.pl/raw').text
}
logger.info("Report on failed function", extra=extra)
